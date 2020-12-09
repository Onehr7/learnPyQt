# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 11:29
# @Author  : Wanghairui
# @function: 子菜单
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu("Import", self)
        impAct = QAction("Import mail", self)
        impMenu.addAction(impAct)

        newAct = QAction("New", self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Submenu")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()