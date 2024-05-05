from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ChiSquare2Var(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.labels = {
            'dep_x_squared': 'Depression X²',
            'dep_p_value': 'Depression p-value',
            'anx_x_squared': 'Anxiety X²', 
            'anx_p_value': 'Anxiety p-value'
        }
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.search_label = QLabel("Search for a question combination:", self)
        self.search_label.setFont(QFont("", 14))
        self.search_field = QLineEdit(self)
        self.search_field.setPlaceholderText("Enter specific format")
        self.search_field.setFont(QFont("", 14))
        self.search_field.textChanged.connect(self.update_combo_box)
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_field)

        # "or" label
        or_label = QLabel("or", self)
        or_label.setAlignment(Qt.AlignHCenter)
        or_label.setFont(QFont("", 14))
        layout.addWidget(or_label)

        # Dropdown box
        self.label = QLabel("Select the question combination:", self)
        self.label.setFont(QFont("", 14))
        layout.addWidget(self.label)

        self.combo_box = QComboBox(self)
        self.combo_box.setFont(QFont("", 14))
        layout.addWidget(self.combo_box)

        self.button = QPushButton("Submit", self)
        self.button.setFont(QFont("", 14))
        self.button.clicked.connect(self.calculate_chi_square)
        layout.addWidget(self.button)

        self.result_label = QLabel(self)
        self.result_label.setFont(QFont("", 14))
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.combo_box.addItems(self.data.index)

        self.setWindowTitle("ChiSquare2Var")

        self.setFixedWidth(450)

    def update_combo_box(self, text):
        self.combo_box.clear()
        matching_items = [item for item in self.data.index if text.lower() in item.lower()]
        self.combo_box.addItems(matching_items)

    def calculate_chi_square(self):
        question_combination = self.combo_box.currentText()

        if question_combination in self.data.index:
            row = self.data.loc[question_combination]
            result_text = ""
            for column, label in self.labels.items():
                value = row[column]
                result_text += f"{label}: <font color='red'>{value}</font><br>"
            self.result_label.setText(result_text)
        else:
            QMessageBox.warning(self, "Error", "Question combination entry not found. Make sure you typed in the correct format")
