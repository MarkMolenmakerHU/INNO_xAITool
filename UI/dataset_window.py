from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi


class DatasetWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(DatasetWindow, self).__init__()
        loadUi('UI/Ui/dataset.ui', self)

        global datasets
        datasets = [self.widget_datasetA, self.widget_datasetB, self.widget_datasetC]

        # Dataset Selection
        for dataset in datasets:
            dataset.installEventFilter(self)

        # Footer Navigation Buttons
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_next.clicked.connect(self.next)

    def eventFilter(self, source, event):
        if source.property("dataset") is not None:
            if event.type() == QEvent.MouseButtonPress:
                # Deselect all datasets
                for dataset in datasets:
                    if dataset.isEnabled() is False:
                        continue
                    dataset.setProperty("selected", False)
                    dataset.setStyleSheet(dataset.styleSheet())

                # Select clicked dataset
                source.setProperty("selected", True)
                source.setStyleSheet(source.styleSheet())
        elif source.property("href-text") is True:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

        return super(DatasetWindow, self).eventFilter(source, event)

    def back(self):
        print("back")

    def next(self):
        print("next")
