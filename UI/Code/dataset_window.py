from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from UI.Code.Components.loader import Loader


class DatasetWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(DatasetWindow, self).__init__()
        loadUi('UI/Design/dataset.ui', self)
        self.stackedWidget = stackedWidget
        self.file_name = None
        self.nextButton.clicked.connect(self.next)
        self.browseButton.clicked.connect(self.browse)
        self.breastCancerWidget.mouseReleaseEvent = self.select
        Loader(self.nextButton)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def browse(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.pathLine.setText(self.file_name)

    def select(self, event):
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.breastCancerWidget.setGraphicsEffect(shadow)
