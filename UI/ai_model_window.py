from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget
from PyQt5.uic import loadUi


class AiModelWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(AiModelWindow, self).__init__()
        loadUi('UI/Ui/ai-model.ui', self)
        self.stackedWidget = stackedWidget
        self.file_name = None
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)
        self.browseButton.clicked.connect(self.browse)

    def prev(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def browse(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.pathLine.setText(self.file_name)
