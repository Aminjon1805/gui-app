import sys
import socket
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatZone - Server")
        self.setGeometry(100, 100, 400, 400)


        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)



        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)




        self.HOST = '127.0.0.1'
        self.PORT = 12345
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(1)

        self.chat_area.append("Server started. Waiting for client...")

        self.conn, self.addr = self.server_socket.accept()
        self.chat_area.append(f"Connected by {self.addr}")




        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()



    def receive_messages(self):
        while True:
            try:
                message = self.conn.recv(1024).decode('utf-8')
                if message:
                    self.chat_area.append(f"Client: {message}")
                else:
                    break
            except:
                break


    def send_message(self):
        msg = self.input_box.text()
        if msg:
            self.conn.sendall(msg.encode('utf-8'))
            self.chat_area.append(f"You: {msg}")
            self.input_box.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec())
