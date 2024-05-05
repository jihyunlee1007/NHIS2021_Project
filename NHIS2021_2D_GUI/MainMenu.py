from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
import urllib.request

from ChiSquare2Var import ChiSquare2Var
from ThreeDGraph import ThreeDGraph
from TwoDGraph import TwoDGraph

class MainMenu(QMainWindow):
    def __init__(self, data, chi_data):
        super().__init__()
        self.data = data
        self.chi_data = chi_data
        self.chi_widget = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2021 National Health Interview Survey (NHIS) 2D GUI")
        self.resize(1900, 1000)

        url = "https://raw.githubusercontent.com/jihyunlee1007/NHIS2021_Project/main/nhis_transparent_icon.png"
        with urllib.request.urlopen(url) as response:
            image_data = response.read()

        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        image_label = QLabel(self)
        scaled_pixmap = pixmap.scaledToHeight(70)
        image_label.setPixmap(scaled_pixmap)

        title_label = QLabel("CDC National Health Interview Survey 2021 Data Analysis", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 28pt; color: #252547; font-weight: bold;")

        title_layout = QHBoxLayout()
        title_layout.addWidget(image_label)
        title_layout.addWidget(title_label)
        title_layout.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.addLayout(title_layout)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addSpacerItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        btn_2d = QPushButton("2D Graph", self)
        btn_2d.clicked.connect(self.show_2d_graph)
        btn_2d.setStyleSheet("background-color: #4D4D99; color: white;")
        btn_2d.setFixedSize(450, 40)
        btn_2d.setFont(QFont("", 14))
        button_layout.addWidget(btn_2d)

        btn_3d = QPushButton("3D Graph", self)
        btn_3d.clicked.connect(self.show_3d_graph)
        btn_3d.setStyleSheet("background-color:#8080CC; color: white;")
        btn_3d.setFixedSize(450, 40)
        btn_3d.setFont(QFont("", 14))
        button_layout.addWidget(btn_3d)

        btn_chisqr = QPushButton("Chi-Square Analysis (2 Variables)", self)
        btn_chisqr.clicked.connect(self.show_chi_square)
        btn_chisqr.setStyleSheet("background-color: #A3A3CC; color: white;")
        btn_chisqr.setFixedSize(450, 40)
        btn_chisqr.setFont(QFont("", 14))
        button_layout.addWidget(btn_chisqr)

        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setStyleSheet("background-color: #CCCCCC;")

        self.setCentralWidget(central_widget)


    def show_2d_graph(self):
        self.two_d_window = TwoDGraph(self.data)
        self.two_d_window.show()

    def show_3d_graph(self):
        self.three_d_window = ThreeDGraph(self.data)
        self.three_d_window.show()

    def show_chi_square(self):
        if self.chi_widget is None:
            self.chi_widget = ChiSquare2Var(self.chi_data)
        self.chi_widget.show()
