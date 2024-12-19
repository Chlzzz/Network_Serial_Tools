from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import threading
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from common import utils
from drivers.driver_serial import *
from ui.Ui_serial_assistant_widget import Ui_SerialAssistantWidget
from views.serial_setting_dialog import SerialSettingDialog


class SerialAssistantWidget(QWidget): # type: ignore

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SerialAssistantWidget()
        self.ui.setupUi(self)
        
        self.sd: SerialDevice = None
        self.init_ui()
        self.refresh_device()

    def refresh_device(self):
        self.devices = scan_serial_ports()
        device_names = [item[1] for item in self.devices]
        self.ui.cb_device.clear()
        self.ui.cb_device.addItems(device_names)
    
    def show_setting_dialog(self):
        dialog = SerialSettingDialog()
        rst = dialog.exec_()
        if rst == QDialog.Accepted: # type: ignore
            print("accept!!")
            self.ui.cb_baud.setCurrentIndex(self.ui.cb_baud.findText(dialog.baudrate))
        else:
            print("reject!!")

    def update_connect_ui(self):
        if self.sd is not None:
            self.ui.btn_connect.setText("断开连接")
        else:
            self.ui.btn_connect.setText("连接设备")

    def run_serial_clicked(self, port, baud_rate):
        
        self.sd = SerialDevice(port, baud_rate=baud_rate)  # 替换为您的串口名称、波特率和超时时间
        if not self.sd.open():
            return
        print("连接成功,等待接收数据")
        self.update_connect_ui()
        try:
            while True:
                data = self.sd.readline()
                if data:
                    msg = utils.decode_data(data)
                    self.ui.edit_recv.append(msg)
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            self.sd.close()
            self.sd = None
            self.update_connect_ui()

    def on_connect_clicked(self):
        if self.sd is not None:
            self.sd.close()
            self.sd = None
            self.update_connect_ui()
            return 
        
        device = self.devices[self.ui.cb_device.CurrentText()]
        print("connect:", device)
        port = device[0]
        baud_rate = int(self.ui.cb_baud.CurrentText())
        thread = threading.Thread(target = self.run_serial_clicked,
                                  args = (port, baud_rate),
                                  daemon = True)
        thread.start()
    
    def on_send_clicked(self):
        if self.sd == None:
            print("请线连接设备")
            QMessageBox.warning(self, "警告", "请线连接设备") # type: ignore
            return 
        
        text = self.ui.edit_send.toPlainText()
        if text == "":
            print("请输入要发送的数据")
            QMessageBox.warning(self, "警告", "请输入要发送的数据") # type: ignore
            return

        self.ui.write(f"{text}\n".encode())     # 发送数据
        
    def init_ui(self):
        self.ui.btn_refresh.clicked.connect(self.refresh_device)
        self.ui.btn_setting.clicked.connect(self.show_setting_dialog)
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)

if __name__ == '__main__':
    app = QApplication(sys.argv) # type: ignore

    window = SerialAssistantWidget()
    window.show()

    sys.exit(app.exec_())