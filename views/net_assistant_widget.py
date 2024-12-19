from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import threading
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from ui.Ui_net_assistant_widget import Ui_NetAssistantWidget
from common.utils import decode_data, get_local_ip


class NetAssistantWidget(QWidget): # type: ignore

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NetAssistantWidget()
        self.ui.setupUi(self)

        self.tcp_client = None

        self.init_ui()

    def update_connect_status(self):
        """
        根据连接状态,更新界面
        """
        if self.tcp_client is not None:
            self.ui.btn_connect.setText("断开连接（已连接）")
        else:
            self.ui.btn_connect.setText("连接网络")

    def run_tcp_client(self, target_ip, target_port):
        # 创建TCP类型socket
        self.tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            targte_addr = (target_ip, int(target_port))
            self.tcp_client.connect(targte_addr)
            print("服务器已连接")

            local_ip, local_port = self.tcp_client.getsockname() # 获取ip
            
            self.ui.local_ip.setCurrentIndex(self.ui.local_ip.findText(local_ip))
            self.ui.local_port.setText(str(local_port))
            self.update_connect_status()
            while True:
                bytes_data = self.tcp_client.recv(2048)
                if bytes_data:    
                    str_data = decode_data(bytes_data)
                    self.ui.edit_recv.append(str_data)
                else:
                    break

        except Exception as e:
            print(e)
        finally:
            print("连接关闭")
            if self.tcp_client is not None:
                self.tcp_client.close()
                self.tcp_client = None
                self.update_connect_status()

    def handle_client_connect(self):
        if self.tcp_client is not None:
                print("断开连接")
                self.update_connect_status()
                self.tcp_client.close()
                self.tcp_client = None
                return
        
        target_ip = self.ui.edit_ip.text()
        target_port = self.ui.edit_port.text()
        print(f"连接服务器 {target_ip}:{target_port}")

        if target_ip == "" or target_port == "":
            print("输入ip以及port")
            return
        tcp_thread = threading.Thread(target = self.run_self.tcp_client, 
                                    args = (target_ip, target_port),
                                    daemon = True
                                    )
        tcp_thread.start()

    def handle_new_client(self, client_socket: socket.socket, client_addr):
        try:
            while True:
                bytes_data = client_socket.recv(2048)
                if bytes_data:
                    msg = decode_data(bytes_data)
                    self.ui.edit_recv.append(msg)
                else:
                    break
        except Exception as e:
            print(e)
        finally:
            print(f"客户端[{client_addr}]断开")
            client_socket.close()

    def run_tcp_server(self, server_ip, server_port):
        tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.bind(server_ip, int(server_port))
        tcp_server.listen(128)
        try:
            while True:
                client_socket, client_addr = tcp_server.accept()
                thread = threading.Thread(target = self.handle_new_client,
                                        args = (client_socket, client_addr),
                                        daemon = True)
                thread.start()
        except Exception as e:
            print(e)
        

    def handle_server_connect(self):
        server_ip = self.ui.edit_ip.text()
        server_port = self.ui.edit_port.text()
        if server_port == "":
            print("输入port")
            return
        server_thread = threading.Thread(target = self.run_tcp_server,
                                         args = (server_ip, server_port),
                                         daemon = True)
        server_thread.start()
        
        

    def on_connect_clicked(self):
        current_mode = self.ui.cb_mode.currentIndex()
        if current_mode == 0:
            self.handle_client_connect()
        elif current_mode == 1:
            self.handle_server_run()

     
    def on_send_clicked(self):
        if self.tcp_client is None:
            print("请先连接")
            return
        
        text = self.ui.edit_send.toPlainText()
        self.tcp_client.send(text.decode("UTF-8"))

    def on_mode_changed(self):
        index = self.ui.cb_mode.cirrentIndex()
        if index == 0:
            self.ui.label_ip.setText("服务器ip:")
            self.ui.label_port.setText("服务器port:")
            self.ui.label_port.setText("本地port:")
            self.ui.label_local_port.show()
            self.ui.local_port.show()
        else:
            self.ui.label_ip.setText("本地ip:")
            self.ui.label_port.setText("本地port:")
            self.ui.label_local_port.hide()
            self.ui.local_port.hide()


    def init_ui(self):
        self.ui.edit_ip.setText("127.0.0.1")
        self.ui.edit_port.setText("8888")
        local_ips = get_local_ip()
        self.ui.local_ip.addItems(local_ips)

        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)

        self.ui.cb_mode.currentIndexChanged.connect(self.on_mode_changed)
        # 切换到客户端模式
        self.ui.layout_client


if __name__ == '__main__':
    app = QApplication(sys.argv) # type: ignore

    window = NetAssistantWidget()
    window.show()

    sys.exit(app.exec_())