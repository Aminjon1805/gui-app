import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatZone")
        self.setWindowIcon(QIcon("cz_title_photo.png"))
        self.setGeometry(700, 300, 500, 500)

        # label = QLabel("Hello ,Welcome to our ChatZone", self)
        # label.setFont(QFont("Arial", 40))
        # label.setGeometry(0, 0, 1500, 200)
        # label.setStyleSheet("color: blue;"
        #                     "background-color: #4bd4e3;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: none")
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #
        #
        # label_2 = QLabel(self)
        # label_2.setGeometry(0, 200, 250, 250)
        # label_2.setScaledContents(True)
        #
        # pixmap = QPixmap("cz_title_photo.png")
        # label_2.setPixmap(pixmap)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel('#1', self)
        label2 = QLabel('#2', self)
        label3 = QLabel('#3', self)
        label4 = QLabel('#4', self)
        label5 = QLabel('#5', self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: purple;")
        label5.setStyleSheet("background-color: yellow;")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
