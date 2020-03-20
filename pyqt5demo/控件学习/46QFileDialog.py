import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QFileDialog')
        self.setup_ui()

    def setup_ui(self):
        # result = QFileDialog.getOpenFileName(self, '选择一个python文件', './',
        #                                      'ALL(*.*);;Images(*.png *.jpg *.jpeg);;Py文件(*.py)')

        # result = QFileDialog.getOpenFileNames(self, '选择一个python文件', './',
        #                                       'ALL(*.*);;Images(*.png *.jpg *.jpeg);;Py文件(*.py)')
        # result = QFileDialog.getOpenFileUrl(self, '选择一个python文件', './',
        #                                     'ALL(*.*);;Images(*.png *.jpg *.jpeg);;Py文件(*.py)')
        # result = QFileDialog.getOpenFileUrls(self, '选择一个python文件', './',
        #                                      'ALL(*.*);;Images(*.png *.jpg *.jpeg);;Py文件(*.py)')

        # 保存文件 
        # result = QFileDialog.getSaveFileName(self, '选择一个python文件', './',
        #                                      'ALL(*.*);;Images(*.png *.jpg *.jpeg);;Py文件(*.py)')

        # 选择文件夹 
        # result = QFileDialog.getExistingDirectory(self, '选择', './')
        # result = QFileDialog.getExistingDirectoryUrl(self, '选择', QUrl('./'))
        # print(result)

        def test():
            fd = QFileDialog(self, '标题', './', 'All(*.*)')
            # fd.show()
            # fd.open()
            # fd.exec_()
            fd.filesSelected.connect(lambda files: print(files))

            # 打开模式或者接受模式
            fd.setAcceptMode(QFileDialog.AcceptSave)  # 保存模式
            fd.setAcceptMode(QFileDialog.AcceptOpen)  # 打开模式

            #  默认后缀
            fd.setDefaultSuffix('txt')

            # 设置文件模式
            fd.setFileMode(QFileDialog.AnyFile)
            fd.setFileMode(QFileDialog.ExistingFile)
            fd.setFileMode(QFileDialog.Directory)
            # fd.setFileMode(QFileDialog.ExistingFiles)

            # 名称过滤器
            fd.setNameFilter('all(*.*)')
            fd.setNameFilters(('ALL(*.*)', 'img(*.jpg *.png)'))

            # 显示信息的详细程度
            fd.setViewMode(QFileDialog.Detail)
            fd.setViewMode(QFileDialog.List)

            #
            fd.setLabelText(QFileDialog.FileName, '自定义名称')
            fd.setLabelText(QFileDialog.Accept, '自定义名称-接受')
            fd.setLabelText(QFileDialog.Reject, '自定义名称-拒绝')
            fd.setLabelText(QFileDialog.FileType, '自定义名称-文件类型')
            fd.setLabelText(QFileDialog.LookIn, '自定义名称-LookIn')

            # 信号
            # 当前路径发生变化
            fd.currentChanged.connect(lambda path_str: print(path_str))
            fd.currentUrlChanged.connect(lambda path_url: print(path_url))
            # 打开选中的文件夹的时候
            fd.directoryEntered.connect(lambda path_url: print(path_url))
            fd.directoryUrlEntered.connect(lambda path_url: print(path_url))

            # 文件过滤器选中的时候
            fd.filterSelected.connect(lambda filter_str: print(filter_str))
            
            # 文件选中的时候
            fd.fileSelected.connect(lambda file_str: print(file_str))
            fd.filesSelected.connect(lambda files: print(files))
            fd.urlSelected.connect(lambda url_str: print(url_str))
            fd.urlsSelected.connect(lambda files: print(files))

            fd.open()
            print('点击按钮')
            pass

        btn = QPushButton(self)
        btn.setText('测试按钮')
        btn.move(10, 10)
        btn.clicked.connect(test)
        pass

    pass


pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
