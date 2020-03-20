import sys
from PyQt5.Qt import *

print('argv', sys.argv)  # [Python文件的名称,入参...]
# 命令行启动的时候后面的跟随的参数

# sys.exit() #退出

app = QApplication(sys.argv)
print('arguments', app.arguments())  # 系统入参
print('arguments', qApp.arguments())  # qt提供的全局qApp


# 中间的操作

window = QWidget()
# window.show()
# 刚创建好的控件没有父控件，需要调用 show()方法
# 没有父控件，则把它作为父控件（窗口）
# 系统具备添加装饰
print('size:',window.size())
window.setWindowTitle('没有父控件自动添加')
window.resize(500,300)
# 也可以作为一个容器用于承载其他的控件
label = QLabel(window)
# 创建的时候添加父控件，也可以不传
# label.show()
label.setWindowTitle("测试")
# 无效:

# 没有设置size的默认在左上角
label.setText("观察我在哪里")
label.resize(100,100)
# move 左上角为0，0

# 子类
# print('__subclasses__()',QObject.__subclasses__())
for mro  in QObject.mro():
    print('mro()',mro)

obj  = QObject()
obj.setProperty("key",'test')
obj.setProperty("key1",'demo')
obj.setProperty('key','非洲')

print('property:',obj.property('key'))
print('dynamicPropertyNames():',obj.dynamicPropertyNames())

# 父控件展示之后，子控件
window.show()
# app.exec_()
# 让整个程序开始执行，开始消息循环
# 不断监测结束到的消息
sys.exit(app.exec_())

if __name__ == '__main__':
    pass