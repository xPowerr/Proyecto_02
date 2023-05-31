import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create push buttons
        self.button_w = QPushButton('W', self)
        self.button_a = QPushButton('A', self)
        self.button_s = QPushButton('S', self)
        self.button_d = QPushButton('D', self)
        self.button_i = QPushButton('I', self)
        self.button_j = QPushButton('J', self)
        self.button_k = QPushButton('K', self)
        self.button_l = QPushButton('L', self)

        # Connect button signals to slots
        self.button_w.clicked.connect(self.send_w)
        self.button_a.clicked.connect(self.send_a)
        self.button_s.clicked.connect(self.send_s)
        self.button_d.clicked.connect(self.send_d)
        self.button_i.clicked.connect(self.send_i)
        self.button_j.clicked.connect(self.send_j)
        self.button_k.clicked.connect(self.send_k)
        self.button_l.clicked.connect(self.send_l)

        # Add buttons to the main window
        self.setCentralWidget(self.button_w)

        # Initialize serial communication
        self.serial = serial.Serial('COM3', 9600)  # Adjust port and baud rate as per your setup

    def send_w(self):
        self.serial.write(b'w')

    def send_a(self):
        self.serial.write(b'a')

    def send_s(self):
        self.serial.write(b's')

    def send_d(self):
        self.serial.write(b'd')

    def send_i(self):
        self.serial.write(b'i')

    def send_j(self):
        self.serial.write(b'j')

    def send_k(self):
        self.serial.write(b'k')

    def send_l(self):
        self.serial.write(b'l')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())