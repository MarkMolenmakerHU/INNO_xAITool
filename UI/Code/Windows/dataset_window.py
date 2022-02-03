from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from Datasets.Code import load_iris, load_breast_cancer, load_titanic, load_stock
from Helpers import load_dataset


class DatasetWindow(BaseWindow):
    defaults = [
        load_iris(),
        load_breast_cancer(),
        load_titanic(),
        load_stock()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'dataset', 'Tabular (*.csv)', 'Datasets/Data')

    def browse_action(self, file_path):
        self.selected_option = load_dataset(file_path)
