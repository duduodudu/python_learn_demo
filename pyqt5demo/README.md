## PyQt5 学习笔记
基于(B站视频)[https://www.bilibili.com/video/av61686342/]的学习笔记
视频录制事件为约为2018年11月，详见:P211 7:52 
- (Mac 下 PyQt5 的开发环境搭建)[https://www.jianshu.com/p/c5001fc182ec]

# 打包发布 pyinstaller 
- 安装:`pip install pyinstaller` 测试:`pyisntaller --version`
- 默认打包:`pyinstaller main.py` 主入口文件
- 可选项: -F -w 
- 自定义模块可能会与系统模块名相同
- qss需要复制到相同的dist文件夹下