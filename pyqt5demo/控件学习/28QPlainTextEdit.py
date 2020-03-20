import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPlainEditText')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(300, 300)
        pte.move(100, 100)
        # 占位提示文本
        pte.setPlaceholderText('占位提示文本')
        # 只读设置
        pte.setReadOnly(True)
        print('是否只读', pte.isReadOnly())
        # 格式: 设置 合并

        # 换行模式
        print('换行模式', pte.lineWrapMode())
        # pte.setLineWrapMode(QPlainTextEdit.NoWrap)
        # 覆盖模式 ####
        pte.setOverwriteMode(True)
        # tab 控制 ######### 
        # 文本操作 ##########
        pte.setPlainText('设置文本')
        pte.insertPlainText('插入文本')
        pte.appendPlainText('追加文本')
        pte.appendHtml('追加html')  # html 不一定全部支持 表格 图 列表 
        print('文本内容', pte.toPlainText())
        # 块操作 #######
        print('块', pte.blockCount())
        pte.setMaximumBlockCount(100)  # 设置最大的段落数量,超出的将覆盖前面的块
        # 常用编辑操作 
        pte.selectAll()
        pte.copy()
        pte.undo()
        # 放大缩小
        pte.zoomIn()
        pte.zoomIn(10)
        pte.zoomIn(-1)
        # 滚动到保证光标可见
        pte.setCenterOnScroll(True)
        pte.centerCursor()  # 是光标所在行处于屏幕中间
        pte.ensureCursorVisible()  # 保证光标可见
        pte.setFocus()
        self.pte = pte
        self.光标操作()
        # 信号
        # 文本内容发生改变
        # pte.textChanged
        # 选中内容改变
        # pte.selectionChanged
        # 编辑状态改变时
        # pte.modificationChanged
        # 光标位置改变时
        # pte.cursorPositionChanged
        # 块的个数改变时
        # pte.blockCountChanged
        # 内容更新请求时
        # pte.updateRequest
        # 复制可用时
        # pte.copyAvailable
        # 重做可用时
        # pte.redoAvailable
        # 撤销可用时
        # pte.undoAvailable
        pass

    def 光标操作(self):
        tc = self.pte.textCursor()
        tc = self.pte.cursorForPosition(QPoint(100, 60))
        tc.insertText('光标插入的文本')
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
