import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGroupBox, QPushButton, QWidget
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtCore import Qt

class CustomGroupBox(QGroupBox):
    def _init_(self, title):
        super()._init_(title)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white)  # Set the text color to white
        painter.drawText(event.rect(), Qt.AlignCenter, self.title())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creat window and name it
        self.setWindowTitle('Control de brazo mecánico con comunicación serial PC-PIC16f887')

        # Create buttons
        self.button_w = QPushButton('Incrementar Servo 2')
        self.button_a = QPushButton('Decrementar Servo 1')
        self.button_s = QPushButton('Decrementar Servo 2')
        self.button_d = QPushButton('Incrementar Servo 1')
        self.button_i = QPushButton('Incrementar Servo 3')
        self.button_j = QPushButton('Decrementar Servo 4')
        self.button_k = QPushButton('Decrementar Servo 3')
        self.button_l = QPushButton('Incrementar Servo 4')
        self.button_z = QPushButton('Cambiar a modo manual')
        self.button_x = QPushButton('Cambiar a modo EEPROM')
        self.button_c = QPushButton('Permanecer en modo UART')
        self.button_v = QPushButton('Cambiar a modo Adafruit')
        

        # Connect button signals to slots
        self.button_w.clicked.connect(self.send_w)
        self.button_a.clicked.connect(self.send_a)
        self.button_s.clicked.connect(self.send_s)
        self.button_d.clicked.connect(self.send_d)
        self.button_i.clicked.connect(self.send_i)
        self.button_j.clicked.connect(self.send_j)
        self.button_k.clicked.connect(self.send_k)
        self.button_l.clicked.connect(self.send_l)
        self.button_z.clicked.connect(self.send_z)
        self.button_x.clicked.connect(self.send_x)
        self.button_c.clicked.connect(self.send_c)
        self.button_v.clicked.connect(self.send_v)

        # Set button colors
        self.set_button_colors()

        # Create group boxes for columns
        column1 = self.create_column('Controlar Servo 1 - Base', [self.button_d, self.button_a])
        column2 = self.create_column('Controlar Servo 2 - Brazo - codo', [self.button_w, self.button_s])
        column3 = self.create_column('Controlar Servo 3 - Brazo - hombro', [self.button_i, self.button_k])
        column4 = self.create_column('Controlar Servo 4 - Garra', [self.button_l, self.button_j])
        column5 = self.create_column('Controlar cambio de modos', [self.button_z, self.button_x, self.button_c, self.button_v])

        # Create layout for columns
        layout = QVBoxLayout()
        layout.addWidget(column1)
        layout.addWidget(column2)
        layout.addWidget(column3)
        layout.addWidget(column4)
        layout.addWidget(column5)

        # Create widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the widget as the central widget
        self.setCentralWidget(widget)

        # Initialize serial communication
        self.serial = serial.Serial('COM3', 9600)  # Adjust port and baud rate as per your setup

        # Set the text color to white
        #self.set_text_color()

    def create_column(self, name, buttons):
        group_box = QGroupBox(name)
        layout = QVBoxLayout()
        for button in buttons:
            layout.addWidget(button)
        group_box.setLayout(layout)
        return group_box

    def set_button_colors(self):
        # Set background colors for buttons
        button_colors = {
            'button_w': QColor(0, 153, 0),     # Green
            'button_a': QColor(255, 0, 0),     # Red
            'button_s': QColor(255, 0, 0),     # Red
            'button_d': QColor(0, 153, 0),     # Green
            'button_i': QColor(0, 153, 0),     # Green
            'button_j': QColor(255, 0, 0),     # Red
            'button_k': QColor(255, 0, 0),     # Red
            'button_l': QColor(0, 153, 0),     # Green
            'button_z': QColor(0, 0, 255),     # Blue
            'button_x': QColor(0, 153, 0),     # Green
            'button_c': QColor(204, 204, 0),   # Yellow
            'button_v': QColor(255, 0, 0),     # Red
        }

        # Apply background colors to buttons
        for button_name, color in button_colors.items():
            button = getattr(self, button_name)
            button.setStyleSheet(f"background-color: {color.name()}; color: white;")

    #def set_text_color(self):
        # Set the text color to white
        #palette = self.palette()
        #palette.setColor(QPalette.ButtonText, Qt.white)
        #palette.setColor(QPalette.WindowText, Qt.white)
        #self.setPalette(palette)

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

    def send_z(self):
        self.serial.write(b'z')

    def send_x(self):
        self.serial.write(b'x')

    def send_c(self):
        self.serial.write(b'c')

    def send_v(self):
        self.serial.write(b'v')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Set background window color
    window.setStyleSheet("background-color: Black; color: white;")

    window.show()
    sys.exit(app.exec_())