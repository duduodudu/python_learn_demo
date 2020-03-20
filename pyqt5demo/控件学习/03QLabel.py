from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.setWindowTitle("QLabel")

label = QLabel(window)
label.setText("测试")
# label.setStyleSheet("font-size:20px;color:red;")

label2 = QLabel(window)
label2.setText("测试2")
label2.setObjectName("warming")
label2.move(100, 100)

labell = QLabel(window)
labell.setText("测试2 level")
labell.setProperty('level', 'notice')
labell.setObjectName("warming")
labell.move(300, 100)

label3 = QLabel(window)
label3.setObjectName('obj')
label3.setText("测试3 id 选择")
label3.move(200, 200)

# label3.setParent(labell)
# 父子关系操作
with open("03Qss.qss", 'r') as f:
    app.setStyleSheet(f.read())

# 直接子对象
for child in window.children():
    print('children:', child)

print('parent:',label.parent())
window2 = QWidget()
window2.setWindowTitle('测试2')
window2.show()
window.show()
sys.exit(app.exec_())
