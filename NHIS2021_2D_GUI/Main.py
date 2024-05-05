import sys
from PyQt5.QtWidgets import QApplication
from DataSet import DataSet
from MainMenu import MainMenu

class Main:
    def __init__(self, dataset_url, chi_dataset_url):
        self.dataset_url = dataset_url
        self.chi_dataset_url = chi_dataset_url
        self.data = None
        self.chi_data = None 
        self.main_window = None

    def load_data(self):
        self.data = DataSet.load_data(self.dataset_url)
        self.chi_data = DataSet.load_data(self.chi_dataset_url, index_col=0)

    def run(self):
        self.load_data()

        app = QApplication(sys.argv)

        self.main_window = MainMenu(self.data, self.chi_data)
        self.main_window.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
    dataset_url = "https://raw.githubusercontent.com/jihyunlee1007/NHIS2021_Project/main/nhisadult21cleaned.csv"
    chi_dataset_url = "https://raw.githubusercontent.com/jihyunlee1007/NHIS2021_Project/main/chi.csv"
    app = Main(dataset_url, chi_dataset_url)
    app.run()
