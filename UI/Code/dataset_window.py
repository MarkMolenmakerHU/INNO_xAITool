from PyQt5.QtWidgets import QLabel, QMainWindow, QFileDialog, QPushButton, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from UI.Code.Components.modal import Modal


class DatasetWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(DatasetWindow, self).__init__()
        loadUi('UI/Design/dataset.ui', self)
        self.stackedWidget = stackedWidget
        self.file_name = None
        self.nextButton.clicked.connect(self.next)
        self.browseButton.clicked.connect(self.browse)

        for child in self.scrollContents.children()[1:]:
            title = child.findChild(QLabel, 'titleLabel').text()
            
            selectButton = child.findChild(QPushButton, 'selectButton')
            selectButton.clicked.connect(lambda event: self.select(event, child, title))
            
            descriptionButton = child.findChild(QPushButton, 'descriptionButton')
            descriptionButton.clicked.connect(lambda event: Modal(stackedWidget, "Dit is wat extra info over de dataset."))
            
            infoLabel = child.findChild(QLabel, 'infoLabel')
            infoLabel.mousePressEvent = self.show_info

    def show_info(self, event):
        Modal(self.stackedWidget, "Dit zijn wat use cases met de dataset.")

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def browse(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.pathLine.setText(self.file_name)

    def select(self, event, child, title):
        shadow = QGraphicsDropShadowEffect(blurRadius=10)
        child.setGraphicsEffect(shadow)
        self.datasetLabel.setText(f"({title})")
