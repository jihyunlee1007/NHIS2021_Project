from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class TwoDGraph(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle("2D Graph")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        var1_layout = QHBoxLayout()
        self.search_label_var1 = QLabel("Search for a variable:", self)
        self.search_field_var1 = QLineEdit(self)
        self.search_field_var1.setPlaceholderText("Enter keyword")
        self.search_field_var1.textChanged.connect(self.update_variable1_combo)
        var1_layout.addWidget(self.search_label_var1)
        var1_layout.addWidget(self.search_field_var1)
        var1_layout.addWidget(QLabel("or"))
        self.variable1_combo = QComboBox()
        var1_layout.addWidget(self.variable1_combo)

        var2_layout = QHBoxLayout()
        self.search_label_var2 = QLabel("Search for a variable:", self)
        self.search_field_var2 = QLineEdit(self)
        self.search_field_var2.setPlaceholderText("Enter keyword")
        self.search_field_var2.textChanged.connect(self.update_variable2_combo)
        var2_layout.addWidget(self.search_label_var2)
        var2_layout.addWidget(self.search_field_var2)
        var2_layout.addWidget(QLabel("or"))
        self.variable2_combo = QComboBox()
        var2_layout.addWidget(self.variable2_combo)

        layout.addLayout(var1_layout)
        layout.addLayout(var2_layout)

        variable_names = list(self.data.columns)
        self.variable1_combo.addItems(variable_names)
        self.variable2_combo.addItems(variable_names)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.variable1_combo.currentIndexChanged.connect(self.plot_graph)
        self.variable2_combo.currentIndexChanged.connect(self.plot_graph)

        self.plot_graph()

    def update_variable1_combo(self, text):
        try:
            self.variable1_combo.clear()
            matching_items = [item for item in self.data.columns if text.lower() in item.lower()]
            if matching_items:
                self.variable1_combo.addItems(matching_items)
        except Exception as e:
            self.show_error_message(e)

    def update_variable2_combo(self, text):
        try:
            self.variable2_combo.clear()
            matching_items = [item for item in self.data.columns if text.lower() in item.lower()]
            if matching_items:
                self.variable2_combo.addItems(matching_items)
        except Exception as e:
            self.show_error_message(e)

    def show_error_message(self, error):
        QMessageBox.critical(self, "Error", f"An error occurred: {str(error)}")

    def plot_graph(self):
        try:
            self.figure.clear()

            var1_name = self.variable1_combo.currentText()
            var2_name = self.variable2_combo.currentText()

            if not var1_name or not var2_name:
                return

            x = self.data[var1_name]
            y = self.data[var2_name]

            ax = self.figure.add_subplot(111)
            sc = ax.scatter(x, y, alpha=0.3)
            ax.set_xlabel(var1_name)
            ax.set_ylabel(var2_name)
            ax.set_title("2D Graph")

            self.canvas.draw()
        except Exception as e:
            self.show_error_message(e)
