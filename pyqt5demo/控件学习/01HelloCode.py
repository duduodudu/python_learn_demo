from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
print(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥")
window.resize(500,500)
window.move(400,300)

label = QLabel(window)
label.setText("Hello dudu")
label.move(200,200)


window.show()
sys.exit(app.exec_())

if __name__ == '__main__':
    pass