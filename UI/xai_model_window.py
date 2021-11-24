from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi


class XaiModelWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget, datasetWindow, aiModelWindow):
        super(XaiModelWindow, self).__init__()
        loadUi('UI/Ui/xai-model.ui', self)
        self.stackedWidget = stackedWidget
        self.datasetWindow = datasetWindow
        self.aiModelWindow = aiModelWindow
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)

    def prev(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        print("Using dataset:", self.datasetWindow.selected_dataset)
        print("Using AI-Model:", self.aiModelWindow.selected_aimodel)
        print("Using xAI-Models", "placeholder")
