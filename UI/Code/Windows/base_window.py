from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from Helpers.ui_helper import bind_selectable
from os.path import split as path_split


class BaseWindow(QMainWindow):
    defaults = []
    selected_child = None
    selected_option = None
    filter = ''

    def __init__(self, stackedWidget: QStackedWidget, window_name: str, filter: str = '', folder_path: str = ''):
        super(BaseWindow, self).__init__()
        loadUi(f'UI/Design/{window_name}.ui', self)
        self.stackedWidget = stackedWidget
        self.filter = filter
        self.folder_path = folder_path
        self.nextButton.setDisabled(True)
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)
        if 'browseButton' in self.__dict__:
            self.browseButton.clicked.connect(self.browse)
        bind_selectable(stackedWidget, self.scrollContents, self.select)

    def prev(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', f'./{self.folder_path}', self.filter)[0]
        if file_path:
            file_name = path_split(file_path)[1].split('.')[0]
            self.pathLine.setText(file_path)
            self.select_action(None, file_name)
            self.browse_action(file_path)

    def browse_action(self, file_path):
        pass

    def select(self, event, index, child, title):
        self.select_action(child, title)
        self.selected_option = self.defaults[index]
        shadow = QGraphicsDropShadowEffect(blurRadius=10)
        child.setGraphicsEffect(shadow)     

    def select_action(self, child, title):
        if self.selected_child is not None: self.selected_child.setGraphicsEffect(None)
        self.stepLabel.setText(f"({title})")
        self.selected_child = child
        self.nextButton.setDisabled(False)
