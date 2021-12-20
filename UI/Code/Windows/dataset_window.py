from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow


class DatasetWindow(BaseWindow):
    defaults = [
        "D:/Documents/School/Hogeschool/Leerjaar 3/Blok 2/Innovation (INNO)/INNO_xAITool/Datasets/iris_dataset.csv"
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'dataset')
