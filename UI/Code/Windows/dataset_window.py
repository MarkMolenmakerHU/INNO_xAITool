from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from sklearn.datasets import load_iris, load_breast_cancer
from Helpers import load_dataset


class DatasetWindow(BaseWindow):
    defaults = [
        load_iris(),
        load_breast_cancer(),
        load_iris(),
        load_iris()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'dataset', 'Tabular (*.csv)')

    def browse_action(self, file_path):
        self.selected_option = load_dataset(file_path)
