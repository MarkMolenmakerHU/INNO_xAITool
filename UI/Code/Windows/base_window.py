from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from Helpers.ui_helper import bind_selectable

class BaseWindow(QMainWindow):
    defaults = []

    def __init__(self, stackedWidget: QStackedWidget, window_name: str):
        super(BaseWindow, self).__init__()
        loadUi(f'UI/Design/{window_name}.ui', self)
        self.stackedWidget = stackedWidget
        self.file_name = None
        self.nextButton.setDisabled(True)
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)
        if 'browseButton' in locals(): 
            self.browseButton.clicked.connect(self.browse)
        bind_selectable(stackedWidget, self.scrollContents, self.select)

    def prev(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def browse(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.pathLine.setText(self.file_name)
        self.nextButton.setDisabled(False)

    def select(self, event, index, child, title):
        shadow = QGraphicsDropShadowEffect(blurRadius=10)
        child.setGraphicsEffect(shadow)
        self.stepLabel.setText(f"({title})")
        self.file_name = self.defaults[index]
        self.nextButton.setDisabled(False)
