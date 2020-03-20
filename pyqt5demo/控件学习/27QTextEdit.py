import sys
from PyQt5.Qt import *


class MyTextEdit(QTextEdit):
    def mousePressEvent(self, e) -> None:
        print(e.pos())
        print(self.anchorAt(e.pos()))
        url_str = self.anchorAt(e.pos())
        if len(url_str) > 0:
            QDesktopServices.openUrl(QUrl(url_str))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        te = MyTextEdit(self)
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet('background-color:cyan;')
        self.te = te

        btn = QPushButton(self)
        btn.move(10, 10)
        btn.setText('按钮')
        btn.pressed.connect(self.btn_clicked)

        self.占位文本的提示()
        self.文本内容的设置()

    def btn_clicked(self):
        print('点击按钮')
        self.超链接()

    def 信号测试(self):
        # 文本发生变化
        # self.te.textChanged
        # 选中的内容发生变化
        # self.te.selectionChanged
        # 光标位置发生变化
        # self.te.cursorPositionChanged
        # 当前字符格式发生变化
        # self.te.currentCharFormatChanged
        # 复制可用时
        # self.te.copyAvailable
        # 重做可用时
        # self.te.copyAvailable
        # 撤销可用时
        # self.te.undoAvailable
        pass

    def 超链接(self):
        self.te.insertHtml("<h1><a href='http://www.baidu.com'>百度</a></h1>")
        # 需要监听信号
        pass

    def tab键位控制(self):
        self.te.setTabChangesFocus(True)
        self.te.setTabStopWidth(100)
        self.te.setTabStopDistance(100)
        pass

    def 只读设置(self):
        # read only 只读
        self.te.setReadOnly(True)
        self.te.insertPlainText('插入文本')
        print('是否只读:', self.te.isReadOnly())
        pass

    def 滚动到锚点(self):
        # <a name='name'> </a>
        self.te.scrollToAnchor('name')
        pass

    def 字符设置(self):
        tcf = QTextCharFormat()
        self.te.setCurrentCharFormat(tcf)
        pass

    def 颜色设置(self):
        self.te.setTextColor(QColor(144, 12, 23))
        self.te.setTextBackgroundColor(QColor(200, 10, 10))
        pass

    def 字体设置(self):
        # 弹出字体选择框
        # QFontDialog.getFont()
        self.te.setFontFamily('幼圆')
        self.te.setFontWeight(QFont.Black)
        self.te.setFontItalic(True)
        self.te.setFontPointSize(20)
        self.te.setFontUnderline(True)
        # 统一设置
        font = QFont()
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)
        pass

    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter)
        print('对齐方式', self.te.alignment())
        pass

    def 光标设置(self):
        # 光标宽度
        self.te.setCursorWidth(10)
        print('光标宽度:', self.te.cursorWidth())
        #
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False)
            self.te.setCursorWidth(1)
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(15)
        pass

    def 覆盖模式(self):
        self.te.setOverwriteMode(True)
        print('是否处于覆盖模式：', self.te.overwriteMode())
        pass

    def 软换行模式(self):
        # 不换行
        self.te.setLineWrapMode(QTextEdit.NoWrap)  # 不换行
        # 固定像素宽度
        self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWidth(100)
        # 固定列的宽度
        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.te.setLineWidth(8)
        # 单词的换行模式
        self.te.setWordWrapMode(QTextOption.WordWrap)

        pass

    def 自动格式化(self):
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)
        pass

    def 开始和结束操作(self):
        tc = self.te.textCursor()
        tc.beginEditBlock()
        tc.insertText('123')
        tc.insertBlock()
        tc.insertText('456')
        tc.endEditBlock()
        tc.insertText('789')

        pass

    def 位置相关(self):
        tc = self.te.textCursor()
        print('是否在段落的结尾', tc.atBlockEnd())
        print('是否在段落的开始', tc.atBlockStart())
        print('是否在文档的结尾', tc.atEnd())
        print('是否在文档的开始', tc.atStart())
        print('在第几列', tc.columnNumber())
        print('光标位置', tc.position())
        print('在文本块的位置', tc.positionInBlock())
        pass

    def 文本字符的删除(self):
        tc = self.te.textCursor()
        tc.deleteChar()  # 如果没有选中的文本,删除光标后一个字符
        tc.deletePreviousChar()  # 如果没有选中的文本，删除光标前一个字符
        self.te.setFocus()
        pass

    def 文本的其他操作(self):
        tc = self.te.textCursor()
        print(tc.selectionStart(), tc.selectionEnd())  # 选中的开始，结束
        tc.clearSelection()  # 清除选中
        tc.removeSelectedText()  # 删除选中文本
        print(tc.hasSelection())
        self.te.setTextCursor(tc)
        self.te.setFocus()
        pass

    def 文本选中内容的获取(self):
        tc = self.te.textCursor()
        # 选中的文本
        print('选中的内容', tc.selectedText())
        # QTextDocumentFragment
        s = tc.selection()
        print(tc.selection().toPlainText())
        #
        print(tc.selectedTableCells())
        pass

    def 文本选中和清空(self):
        tc = self.te.textCursor()
        # tc.setPosition(6, QTextCursor.MoveAnchor) # 移动锚点
        # tc.setPosition(6, QTextCursor.KeepAnchor) # 保持锚点
        # 移动 位置，锚点
        tc.movePosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor, 1)
        # 此处需要设置回去才会有效果的
        self.te.setTextCursor(tc)
        self.te.setFocus()
        pass

    def 内容和格式的获取(self):
        # 获取格式
        tc = self.te.textCursor()
        tc.block()
        print(tc.block().text())  # 光标所在的文本
        print(tc.blockNumber())
        tc.currentList()  # 文本列表
        tc.currentList().count()
        tc.blockFormat()
        tc.blockCharFormat()
        tc.charFormat()
        tc.blockCharFormat()
        pass

    def 格式设置和合并(self):
        # 格式合并
        tc = self.te.textCursor()
        # tc.mergeBlockCharFormat()
        # tc.mergeBlockFormat()
        # tc.mergeCharFormat()
        return None
        #
        tc = self.te.textCursor()
        tcf = QTextCharFormat()

        tc.setCharFormat(tcf)
        return None
        # block format #####
        tc = self.te.textCursor()
        tbf = QTextBlockFormat()
        tc.setBlockFormat(tbf)
        return None
        # char format ####
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily('幼圆')
        tcf.setFontPointSize(24)
        tcf.setFontOverline(True)  # 上划线
        tcf.setFontUnderline(True)  # 下划线
        tc.setBlockCharFormat(tcf)
        pass

    def 光标插入(self):
        tc = self.te.textCursor()
        tff = QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(100, 50, 50))
        tff.setRightMargin(50)
        tc.insertFrame(tff)
        doc = self.te.document()
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)
        return None
        # 插入 文本块 ##################
        tc = self.te.textCursor()
        tc.insertBlock()
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)
        tbf.setRightMargin(100)
        tbf.setIndent(1)
        tc.insertBlock(tbf)
        self.te.setFocus()
        return None
        # 插入表格 ##############
        tc = self.te.textCursor()
        # tc.insertTable(5, 3)  # 行，列
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellSpacing(2)
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
                                       QTextLength(QTextLength.PercentageLength, 20),
                                       QTextLength(QTextLength.PercentageLength, 30)))
        table = tc.insertTable(5, 3, ttf)  # 行，列
        # table.appendColumns(3)  # 追加

        return None

        # 插入列表 #######
        tc = self.te.textCursor()
        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix('<<')
        tl = tc.createList(tlf)

        # 插入
        # tl = tc.insertList(QTextListFormat.ListCircle)
        # tl = tc.insertList(QTextListFormat.ListDecimal)
        # 创建
        # tl = tc.createList(QTextListFormat.ListDecimal)

        return None
        # 插入句子
        tc = self.te.textCursor()
        tdd = QTextDocumentFragment.fromHtml('文本片段')
        tc.insertFragment(tdd)
        return None
        # 插入图片
        tc = self.te.textCursor()
        tif = QTextImageFormat()
        tif.setWidth(100)
        tif.setHeight(100)
        tif.setName('images/demo.png')

        tc.insertImage(tif)
        return None
        # 插入文本
        tcf = QTextCharFormat()
        tcf.setToolTip('提示信息')
        tcf.setFontFamily('隶书')
        tcf.setFontPointSize(24)
        tc = self.te.textCursor()
        tc.setCharFormat(tcf)
        tc.insertHtml('<h4>插入文本</h4>')

    def 文本内容的设置(self):
        # 普通文本
        self.te.setPlainText('<h1>XXX</h1>')
        self.te.insertPlainText('<h1>插入的文本</h1>')
        # print('toPlainText:', self.te.toPlainText())
        # 富文本
        self.te.setHtml('<h1>富文本</h1>')
        self.te.insertHtml('<h1>插入的富文本</h1>')
        # print('toHtml:', self.te.toHtml())
        # 设置文本  自动判定
        self.te.setText('<h2>自动判定</h2>')
        # 追加文本 append
        self.te.append('在末尾追加的文本')
        self.te.append('<h3>在末尾追加的文本</h3>')
        # 清空文本 clear
        self.te.setText('')
        self.te.clear()
        # 文档对象 QTextDocument
        # print('document:', self.te.document())
        # 光标对象 QTextCursor
        # print('textCursor:', self.te.textCursor())

    def 占位文本的提示(self):
        self.te.setPlaceholderText('请输入你的个人简介')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    # QTextEdit
    # 支持 Html4 富文本 a,h1,css,(考虑webkit)
    # 段落和字符，支持大文档
    # 加载纯文本和富文本文件 

    window.show()
    sys.exit(app.exec_())
