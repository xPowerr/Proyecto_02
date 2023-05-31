import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGroupBox, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creat window and name it
        self.setWindowTitle('Control de brazo mecánico con comunicación serial PC-PIC16f887')

        # Create buttons
        self.button_w = QPushButton('Incrementar Servo 2')
        self.button_a = QPushButton('Incrementar Servo 1')
        self.button_s = QPushButton('Decrementar Servo 2')
        self.button_d = QPushButton('Decrementar Servo 1')
        self.button_i = QPushButton('Incrementar Servo 3')
        self.button_j = QPushButton('Incrementar Servo 4')
        self.button_k = QPushButton('Decrementar Servo 3')
        self.button_l = QPushButton('Decrementar Servo 4')

        # Connect button signals to slots
        self.button_w.clicked.connect(self.send_w)
        self.button_a.clicked.connect(self.send_a)
        self.button_s.clicked.connect(self.send_s)
        self.button_d.clicked.connect(self.send_d)
        self.button_i.clicked.connect(self.send_i)
        self.button_j.clicked.connect(self.send_j)
        self.button_k.clicked.connect(self.send_k)
        self.button_l.clicked.connect(self.send_l)

        # Create group boxes for columns
        column1 = self.create_column('Controlar Servo 1 - Base', [self.button_a, self.button_d])
        column2 = self.create_column('Controlar Servo 2 - Brazo principal', [self.button_w, self.button_s])
        column3 = self.create_column('Controlar Servo 3 - Brazo secundario', [self.button_i, self.button_k])
        column4 = self.create_column('Controlar Servo 4 - Garra', [self.button_j, self.button_l])

        # Create layout for columns
        layout = QVBoxLayout()
        layout.addWidget(column1)
        layout.addWidget(column2)
        layout.addWidget(column3)
        layout.addWidget(column4)

        # Create widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the widget as the central widget
        self.setCentralWidget(widget)

        # Initialize serial communication
        self.serial = serial.Serial('COM3', 9600)  # Adjust port and baud rate as per your setup

    def create_column(self, name, buttons):
        group_box = QGroupBox(name)
        layout = QVBoxLayout()
        for button in buttons:
            layout.addWidget(button)
        group_box.setLayout(layout)
        return group_box

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