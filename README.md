## 使用

There is, currently, no English readme for I am lazy. 🥇

🕹看下面的视频就知道怎么用了，用不着看字

### UI截图
![qwe.jpg](readme.assets/qwe.jpg)

### 采集
1. 启动后自动尝试连接设备，连接后跳转到设置页面，状态栏显示Connected
  > 未连接设备时，无法点击进入设置、曲线、表格页面

2. 设置采集卡参数

3. 点击左下角开始采集后跳转到曲线页面，按设定的采样方式、采样率，连续采集直到达到设定的采样数量
  > 状态栏有提示采样时间进度，另外如果采集到一半卡住不采集了，大概率是代码烂优化，电脑渣性能。建议减少显示通道，降低采样频率，节制总采样数

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/采集.mp4"></video>

### 查看数据

#### 曲线页面

- 勾选要查看的通道
- 用滚动条快速选择范围
- 在曲线上左键拖动，滚轮比例缩放，右键拖动按轴缩放

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/查看曲线.mp4"></video>

#### 表格页面

所有通道的数值

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/查看表格.mp4"></video>

### 导出数据

曲线页面上的保存按钮，保存当前的曲线视图为`png`、`svg`图像。表格页面的导出按钮，可以导出这次采样的所有数据，支持`csv`和`numpy`格式

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/导出数据.mp4"></video>

### 设置参数

设置页面上可以设置采集卡的参数。每次软件启动后，采集卡参数默认加载软件目录下的`profile.json`，配置文件路径提示在文本框中

手动保存当前参数到其他配置文件，或者手动加载了其他被指文件后，文本框中的配置文件路径会改变

> 无论是否切换或手动保存配置文件，软件退出时，当前的参数自动存储到文本框显示的文件路径中

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/设置参数.mp4"></video>

#### 提示和帮助

左侧菜单展开后有界面提示

右侧面板为帮助

👇👇👇此处视频见[./readme.assets](./readme.assets)👇👇👇

<video src="./readme.assets/提示和帮助.mp4"></video>

## 部署

安装[requirements.txt](./requirements.txt)，运行[main.py](main.py)
```shell
$ pip3 install -r requirements.txt
$ python3 main.py
```

## 移植

仓库里用的采集卡是[ULM7606](https://item.taobao.com/item.htm?spm=a230r.1.14.14.73ea353bKt7jRw&id=658679596191&ns=1&abbucket=15#detail)，这个框架还试过几个别的采集卡，为了兼容各种卡的api调用方式，所以[Ulm7606Wrap.py](daq/Ulm7606Wrap.py)的读取数据的方法看上去不太简洁，[DataAcquisition.py](daq/DataAcquisition.py)旨在提供统一的采集卡接口。✈但是在[main.py](main.py)里，还用到了部分继承自`Ulm7606Wrap`的方法，不难发现，优不优雅啥的对我而言不重要。如果你看着挺难受，可以施舍个pull request

当时我只想赶紧把代码糊弄完⚽，用来验证各种采集卡，最后也不出意料的把这个项目开源了。虽说搞了好几个卡，但这个仓库里只剩下了ULM7606，一方面是ULM7606的厂家竟然没有python的例子，这个仓库就开出源来当个第三方的demo，方便看到的有缘人。另一方面这个卡它很便宜，但比有的贵不少倍的卡稳定，而且资料里面有原理图，倒是挺有开源精神的。只要自己弄个驱动、撸个stm32代码，🚀四舍五入就是买了个方案

回到正题，如果想移植到别的采集卡。替换采集卡的dll或者so，放在[daq](./daq)文件夹里。然后写个wrap，读取数据的时候要能和无参调用[Ulm7606Wrap.py](daq/Ulm7606Wrap.py)的`read_fifo`一样不阻塞。然后就去翻屎山[main.py](main.py)把，祝你好运 💪💪

🏁🏁不过这些代码设计的时候是方便移植的，把报的错都解决掉大概就可以了

## 感谢

@[Wanderson Magalhaes](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6) Thanks for the excellent GUI *PyDracula* 🎉🎉<br>@[Karllzy](https://github.com/karllzy) Your intriguing github avatar is really a great pick-me-up 🤣<br>@Anyone who issue, star, folk, and pull request

