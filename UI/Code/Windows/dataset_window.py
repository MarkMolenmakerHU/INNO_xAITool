from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from UI.Code.Windows.images_window import ImageSelectionWindow


class DatasetWindow(BaseWindow):
    defaults = [
        "D:/Documents/School/Hogeschool/Leerjaar 3/Blok 2/Innovation (INNO)/INNO_xAITool/Datasets/iris_dataset.csv"
    ]

    def openImagesSelection(self):
        ImageSelectionWindow(self)

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'dataset')
        self.openImageSelectionBtn.clicked.connect(self.openImagesSelection)
