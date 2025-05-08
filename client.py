import sys
import socket
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatZone - Client")
        self.setGeometry(150, 150, 400, 400)

        # Widgets
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Socket setup
        self.HOST = '127.0.0.1'
        self.PORT = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))

        self.chat_area.append(f"Connected to server {self.HOST}:{self.PORT}")

        # Start receiving thread
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.chat_area.append(f"Server: {message}")
                else:
                    break
            except:
                break

    def send_message(self):
        msg = self.input_box.text()
        if msg:
            self.client_socket.sendall(msg.encode('utf-8'))
            self.chat_area.append(f"You: {msg}")
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec())
