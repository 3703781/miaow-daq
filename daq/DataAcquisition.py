"""
DataAcquisitionDevice
==========
DAQ设备类
作者Miaow
日期2023/01/23
版本1.0.0
---------
测试和例子，连接采集卡后运行::
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>>
    >>> data = []
    >>> daq = DataAcquisitionDevice()
    >>> daq.connect()
    >>> daq.set_config(period=100, cycles=1000)
    >>> if daq.connected:
    ...     for i in range(10):
    ...         data.append(daq.get_data(10))
    >>> np.concatenate(data, axis=0).shape
    (10000, 8)
    >>> a = plt.plot(np.concatenate(data, axis=0)[:, 7] / 65536 * 20)
    >>> plt.show()
    >>>
    >>> daq.disconnect()
"""
import time

import daq.Ulm7606Wrap as Ulm7606Wrap


class DataAcquisitionDevice(Ulm7606Wrap.Ulm7606Wrap):
    """
    DAQ设备类，用于ULM7606
    设备具有以下只读属性, 要访问属性，必须先调用connect方法，然后set_config方法后才能读取:
    1. range: 量程 "+5v~-5v" 或 "+10v~-10v"
    2. over_sampling: 过采样 1, 2, 4, 8, 16, 32 或 64
    3. trig_direction: 触发方式 "falling", "rising" 或 "both"
    4. trig_mode: 触发源 "internal" 或 "both"
    5. sample_period: 采样周期, 单位为微秒, 10 <= period <= 5000
    6. cycles: 触发次数, 0 < cycles <= 2097152
    7. connected: 连接状态, True 或者 False
    8. sample_rate: 采样率, 单位为Hz
    """

    def __init__(self):
        super().__init__()

    def set_config(self, **kwargs):
        """
        对于ULM7606, 以下均为可选参数, 各参数默认值见Ulm7606Wrap类的adc_set_config方法
        :param range_: 量程 "+5v~-5v" 或 "+10v~-10v"
        :param os_: 过采样 1, 2, 4, 8, 16, 32 或 64
        :param trig_dir: 触发方式 "falling", "rising" 或 "both"
        :param trig_mode: 触发源 "internal" 或 "both"
        :param period: 触发周期, 单位为微秒, 10 <= period <= 5000
        :param cycles: 触发次数, 0 < cycles <= 2097152
        """
        self.adc_set_config(**kwargs)
        config_dict = self.adc_get_config()
        [self.__setattr__("_DataAcquisitionDevice__" + k, config_dict[k]) for k in config_dict.keys()]

    @property
    def range(self):
        return self.__getattr__("__range_")

    @property
    def over_sampling(self):
        return self.__os_

    @property
    def trig_direction(self):
        return self.__trig_dir

    @property
    def trig_mode(self):
        return self.__trig_mode

    @property
    def sample_period(self):
        return self.__period

    @property
    def sample_rate(self):
        return 1000000 / self.__period

    @property
    def cycles(self):
        return self.__cycles

    @property
    def connected(self):
        try:
            self.adc_read()
            return True
        except IOError:
            return False

    def connect(self):
        """
        连接设备，在调用get_data方法前必须先调用此方法
        :exception: IOError
        """
        self.scan_dev()
        self.open_dev()
        self.adc_set_config()

    def disconnect(self):
        """
        断开设备连接
        :exception: IOError
        """
        self.close_dev()

    def get_data(self, timeout=0.2):
        """
        阻塞获取数据
        :param timeout: 超时时间, 单位秒
        :exception IOError, FunctionTimedOut
        :return: shape为(self.cycles, 8)的int16 ndarray
                 ndarray中行对应各次采样, 列对应通道1到通道8, 取值范围为-32768~32767, 对应当前量程属性range的电压范围
        """
        self.adc_start()
        return self.read_fifo(self.__cycles, timeout)
