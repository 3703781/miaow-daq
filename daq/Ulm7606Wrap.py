"""
Ulm7606Wrap
==========
包装了ULM7606.dll, 提供了一些新的功能, 如Ulm7606Wrap类中read_fifo的超时功能
作者Miaow
日期2023/01/23
版本1.0.0
---------
测试和例子, 连接采集卡后运行::
    >>> import matplotlib.pyplot as plt
    >>> period = 1000
    >>> cycles = 1000
    >>>
    >>> # 启动
    >>> wrap = Ulm7606Wrap()
    >>> wrap.scan_dev()
    >>> res = wrap.open_dev()
    >>> # 设置
    >>> wrap.adc_set_config(range_="+10v~-10v", os_=1, trig_dir="rising", trig_mode="internal", period=period, cycles=cycles)
    >>>
    >>> # 多次采集
    >>> wrap.adc_start()
    >>> data1 = wrap.read_fifo(cycles, timeout=10)
    >>> wrap.adc_start()
    >>> data2 = wrap.read_fifo(cycles, timeout=10)
    >>> wrap.adc_start()
    >>> data3 = wrap.read_fifo(cycles, timeout=10)
    >>>
    >>> # 画最通道8的图
    >>> a = plt.plot(data1[:, 7] / 65536 * 20)
    >>> plt.show()
    >>> b = plt.plot(data2[:, 7] / 65536 * 20)
    >>> plt.show()
    >>> c = plt.plot(data3[:, 7] / 65536 * 20)
    >>> plt.show()
    >>>
    >>> # 关闭
    >>> wrap.close_dev()
"""
from ctypes import *
from typing import Tuple, Optional

import numpy as np
from func_timeout import func_timeout


class Ulm7606Wrap(object):
    class Ulm7606Config(Structure):
        _fields_ = [
            # bit4: 0:+5v~-5v, 1:+10v~-10v
            # bit 0~2: AD7606过采样 000: None, 001:2x, 010:4x, 011:8x, 100:16x, 101:32x, 110:64x
            ("adc_options", c_uint8),

            # bit2~3: 00:下降沿, 01:上升沿, 10:上升沿和下降沿
            # bit0~1: 00:内时钟, 01:开关和内时钟
            ("trig_options", c_uint8),

            # 采样周期, 单位为微秒, 范围最小10, 最大5000
            ("period", c_uint16),

            # reserved
            ("reserved", c_uint16),

            # 采样次数
            ("cycles", c_uint32),
        ]

    def __init__(self):
        self.dll = cdll.LoadLibrary("./daq/ULM7606.dll")
        self.byte_array_buffer = (c_int16 * 16777216)(0)

    # def __del__(self):
    #     self.dll_handle = cdll.kernel32.GetModuleHandleW("ULM7606.dll")
    #     cdll.kernel32.FreeLibrary(self.dll_handle)

    # int USBScanDev(int NeedInit);
    def scan_dev(self):
        """
        扫描 USB 总线上连接的 ULM7606 设备
        :exception: 若检测到设备数不是1, 报IOError
        """
        res = self.dll.USBScanDev(1)
        if res != 1:
            raise IOError(f"USBScanDev returns {res}")

    # int USBOpenDev(int DevIndex)
    def open_dev(self):
        """
        打开 ULM7606 采集卡设备
        :exception: 发生错误, 则报IOError
        """
        res = self.dll.USBOpenDev(0)
        if res != 0:
            raise IOError(f"USBOpenDev returns {res}")

    # BOOL ULM7606_InitFIFO(BYTE byIndex)
    def init_fifo(self):
        """
        初始化采集卡和 DLL 中的 FIFO 存储空间. 
        用户程序启动时需要调用此函数以初始化相应 FIFO. 
        :exception: 发生错误, 则报IOError
        """
        res = self.dll.ULM7606_InitFIFO(0)
        if res != 1:
            raise IOError(f"InitFIFO returns {res}")

    # BOOL ULM7606_ADCGetConfig(BYTE byIndex,ADC_CONFIG* pCfg)
    def adc_get_config(self) -> dict:
        """
        读取采集卡的配置数据
        :exception: 发生错误, 则报IOError
        :return: 量程, 过采样倍率, 触发方式, 触发源, 采样周期, 采样次数 具体见adc_set_config函数
        """
        config = Ulm7606Wrap.Ulm7606Config()
        res = self.dll.ULM7606_ADCGetConfig(0, byref(config))
        if res != 1:
            raise IOError(f"ADCGetConfig returns {res}")

        range_ = "+5v~-5v" if (config.adc_options >> 4) & 1 == 0 else "+10v~-10v"
        os_ = 2 ** (config.adc_options & 0b111)
        if (config.trig_options & 0b1100) == 0:
            trig_dir = "falling"
        elif (config.trig_options & 0b1100) == 0b0100:
            trig_dir = "rising"
        else:
            trig_dir = "both"
        trig_mode = "internal" if (config.trig_options & 0b11) == 0 else "both"
        period = config.period
        cycles = config.cycles

        return {"range_": range_, "os_": os_, "trig_dir": trig_dir, "trig_mode": trig_mode, "period": period, "cycles": cycles}

    # BOOL ULM7606_ADCSetConfig(BYTE byIndex, ADC_CONFIG * pCfg)
    def adc_set_config(self, *, range_: str = "+10v~-10v", os_: int = 1, trig_dir: str = "rising", trig_mode: str = "internal", period: int = 1000, cycles: int = 200):
        """
        将配置数据写入采集卡中
        输入参数不正确, 则报AssertionError
        :param range_: 量程 "+5v~-5v" 或 "+10v~-10v"
        :param os_: 过采样 1, 2, 4, 8, 16, 32 或 64
        :param trig_dir: 触发方式 "falling", "rising" 或 "both"
        :param trig_mode: 触发源 "internal" 或 "both"
        :param period: 触发周期, 单位为微秒, 10 <= period <= 5000
        :param cycles: 触发次数, 0 < cycles <= 2097152
        :exception  输入参数不正确, 则报AssertionError, 其他错误, 则IOError
        """
        assert range_ in ("+5v~-5v", "+10v~-10v")
        assert os_ in (1, 2, 4, 8, 16, 32, 64)
        assert trig_dir in ("falling", "rising", "both")
        assert trig_mode in ("internal", "both")
        assert 10 <= period <= 5000 and isinstance(period, int)
        assert 0 < cycles <= 2097152 and isinstance(cycles, int)

        os_map = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4, 32: 5, 64: 6}
        trig_dir_map = {"falling": 0, "rising": 0b0100, "both": 0x1000}
        config = Ulm7606Wrap.Ulm7606Config(0, 0, 0, 0, 0)
        if range_ == "+10v~-10v":
            config.adc_options = config.adc_options | 0b10000
        config.adc_options |= os_map[os_]
        config.trig_options |= trig_dir_map[trig_dir]
        config.period = period
        config.cycles = cycles

        res = self.dll.ULM7606_ADCSetConfig(0, pointer(config))
        if res != 1:
            raise IOError(f"ADCSetConfig returns {res}")

    # BOOL ULM7606_GetFIFOLeft(BYTE byIndex,DWORD* pdwBuffsize)
    def get_fifo_left(self) -> int:
        """
        获取 FIFO 空间中的剩余数据量, 也就是已经采集的数据量减去已经读取的数据量的差值
        单位为字节数. 每次读取 FIFO 前需要调用此函数确定一下目前 FIFO 中有多少字节的数据需要读取. 
        :exception 发生错误, 则IOError
        :return: FIFO 空间中的剩余字节数
        """
        left_buffer = c_uint16(0)
        res = self.dll.ULM7606_GetFIFOLeft(0, pointer(left_buffer))
        if res != 1:
            raise IOError(f"GetFIFOLeft returns {res}")

        return left_buffer.value

    # BOOL ULM7606_ReadFIFO(BYTE byIndex,BYTE* lpBuffer,DWORD dwBuffSize,DWORD* pdwRealSize)
    def read_fifo(self, sample_count: Optional[int] = None, timeout: Optional[float] = None) -> Optional[np.ndarray]:
        """
        从 FIFO 中读取采样数据. 

        1. 若sample_count设为None, 则不能设置超时, 会自动根据get_fifo_left函数的返回值进行读取, 若get_fifo_left函数的返回值为0, 则立刻返回None
        2. 若sample_count不为None, 可以选择设置超时时间timeout, 在发生超时前, 函数会阻塞读取数据直到读到(sample_count * 16)个字节. 如果超时, raise FunctionTimedOut
        3. 若sample_count不为None, 且没有设置超时时间timeout, 函数会立刻读取一次（不阻塞）然后返回, 读取量可能小于sample_count, 没有读到数据就返回None
        4. 若sample_count不为None, 设置超时时间小于0, 则相当于超时时间为无穷. 

        在不设置超时的情况下, 若没有读到数据, 函数返回None；设置了超时的情况下, 不会返回None, 除非指定的sample_count <= 0
        上述逻辑如下::
            if sample_count is None:
                assert timeout is None
                1) 不阻塞地读取一次, 自动根据get_fifo_left函数的返回值进行读取, 返回None或ndarray
            else:
                if timeout is None:
                    3) 不阻塞地读取一次, 读取量可能小于sample_count, 返回None或ndarray
                elif timeout < 0:
                    4) 阻塞读取但不计时间, 直到读取到sample_count个采样, 返回ndarray
                else:
                    2) 带超时的阻塞读取, 若超时前读取到sample_count个采样, 返回ndarray, 否则raise FunctionTimedOut

        :param sample_count: 要读取的采样数. 一次采样为8个通道同时采样, 但采样数记作1. 
        :param timeout: 超时时间, 单位秒
        :exception IOError, FunctionTimedOut
        :return: None 或者 shape为(小于等于sample_count, 8)的int16 ndarray
                 ndarray中行对应各次采样, 列对应通道1到通道8, 取值范围为-32768~32767, 对应adc_set_config函数中设置的电压范围
        """

        real_size = c_uint32(0)
        if sample_count is None:
            bytes_num = self.get_fifo_left()
        else:
            bytes_num = sample_count * 16
        if bytes_num <= 0:
            return None

        my_nparray = np.empty((1, 1))

        def tmp():
            nonlocal my_nparray
            self.dll.ULM7606_ReadFIFO(0, pointer(self.byte_array_buffer), bytes_num, pointer(real_size))
            # if res != 1:
            #     raise IOError(f"ReadFIFO returns {res}")
            if real_size.value <= 0:
                return None
            my_nparray = np.ctypeslib.as_array(self.byte_array_buffer[:real_size.value // 2]).copy().astype(np.int16)
            return True

        def while_tmp():
            nonlocal bytes_num, my_nparray
            my_nparray_list = []
            while bytes_num > 0:
                self.dll.ULM7606_ReadFIFO(0, pointer(self.byte_array_buffer), bytes_num, pointer(real_size))
                # if res != 1:
                #     raise IOError(f"ReadFIFO returns {res}")
                bytes_num -= real_size.value
                my_nparray_list.append(np.ctypeslib.as_array(self.byte_array_buffer[:real_size.value // 2]).copy().astype(np.int16))
            my_nparray = np.concatenate(my_nparray_list, axis=None)

        if sample_count is None:
            assert timeout is None
            if tmp() is None:
                return None
        else:
            if timeout is None:
                if tmp() is None:
                    return None
            elif timeout < 0:
                while_tmp()
            else:
                func_timeout(timeout, while_tmp)
        return my_nparray.reshape(-1, 8)

    # BOOL ULM7606_ADCRead(BYTE byIndex, WORD * pwValue)
    def adc_read(self):
        """
        采集并读取一次数据, 这个函数可以直接调用, 不用先执行adc_start函数
        :exception IOError
        :return: 一次采集的数据, shape为(1, 8)的int16 ndarray, 列对应通道1到通道8
        """
        res = self.dll.ULM7606_ADCRead(0, pointer(self.byte_array_buffer))
        if res != 1:
            raise IOError(f"ADCRead returns {res}")
        return np.ctypeslib.as_array(self.byte_array_buffer[:8]).astype(np.int16).reshape(1, 8)

    # BOOL ULM7606_ADCStart(BYTE byIndex)
    def adc_start(self):
        """
        启动采集卡开始采集数据, 数据会不断地写入到驱动的 FIFO 中, 直到达到adc_set_config函数设置的触发次数
        :exception 发生错误, 则IOError
        """
        res = self.dll.ULM7606_ADCStart(0)
        if res != 1:
            raise IOError(f"ADCStart returns {res}")

    # BOOL ULM7606_ADCStop(BYTE byIndex)
    def adc_stop(self):
        """
        停止采集卡采集数据, 再次启动时先前采集的数据全部清空且采集卡内部状态机回到 0 态. 
        :exception 如果当前实际上不在采集, 调用该函数会报IOError
        """
        res = self.dll.ULM7606_ADCStop(0)
        if res != 1:
            raise IOError(f"ADCStop returns {res}")

    # BOOL ULM7606_ADCReset(BYTE byIndex)
    def adc_reset(self):
        """
        复位采集卡的 AD7606 器件. 
        :exception 发生错误, 则IOError
        """
        res = self.dll.ULM7606_ADCReset(0)
        if res != 1:
            raise IOError(f"ADCReset returns {res}")

    # int USBCloseDev(int DevIndex)
    def close_dev(self):
        """
        关闭 ULM7606 采集卡设备. 
        :exception: 发生错误, 则报IOError
        """
        res = self.dll.USBCloseDev(0)
        if res != 0:
            raise IOError(f"USBCloseDev returns {res}")
