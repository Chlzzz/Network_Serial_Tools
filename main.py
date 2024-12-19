"""
MainWindow -> ToolBar, MenuBar, StausBar

1. 网络工具
2. 串口工具

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui.Ui_main_window import Ui_MainWindow
from views.net_assistant_widget import NetAssistantWidget
from views.serial_assistant_widget import SerialAssistantWidget


class MainWindow(QMainWindow): # type: ignore

    def __init__(self):
        super().__init__()
        # 创建对象
        self.ui = Ui_MainWindow()
        # 初始化内容
        self.ui.setupUi(self)
        # 初始化ui
        self.init_ui()
    

    def init_ui(self):
        self.ui.tabWidget.addTab(NetAssistantWidget(self), "网络助手")
        self.ui.tabWidget.addTab(SerialAssistantWidget(self), "串口助手")
        

def main():
    app = QApplication(sys.argv) # type: ignore
    window = MainWindow()
    window.resize(1100, 800)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()