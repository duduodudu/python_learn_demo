import sys
from PyQt5.Qt import *


class MySlider(QSlider):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.setTickPosition(QSlider.TicksBothSides)
        label = QLabel(self)
        self.label = label
        label.hide()
        pass

    def mousePressEvent(self, evt) -> None:
        super().mousePressEvent(evt)
        self.change()

    def change(self):
        x = (self.width() - self.label.width()) / 2
        v = self.value() / (self.maximum() - self.minimum())
        if not self.invertedAppearance():
            v = 1 - v
        y = (self.height() - self.label.height()) * v
        print(x, y)
        self.label.move(x, y)
        self.label.setText(str(self.value()))
        self.label.adjustSize()
        self.label.show()

    def mouseMoveEvent(self, evt) -> None:
        super().mouseMoveEvent(evt)
        self.change()

    def mouseReleaseEvent(self, ev) -> None:
        super().mouseReleaseEvent(ev)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('Slider 案例')
        self.setup_ui()

    def setup_ui(self):
        slider = MySlider(self)
        slider.move(100, 100)
        slider.resize(30, 200)

        self.slider = slider

        label = QLabel(self)
        self.label = label
        label.setText('0')
        slider.valueChanged.connect(self.slider_changed)
        pass

    def slider_changed(self, val):
        self.label.setText('当前值:', str(val))
        self.label.adjustSize()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
