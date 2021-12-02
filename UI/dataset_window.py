from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi


class PopupWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PopupWindow, self).__init__(parent)
        loadUi('UI/Ui/info-popup.ui', self)


class DatasetWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(DatasetWindow, self).__init__()
        loadUi('UI/Ui/dataset.ui', self)
        self.stackedWidget = stackedWidget

        # Variables to be used in other windows
        self.selected_dataset = None

        # Dataset Selection
        global datasets
        datasets = [self.widget_datasetA, self.widget_datasetB, self.widget_datasetC]
        for dataset in datasets:
            dataset.installEventFilter(self)

        # Dataset Href
        self.pushButton_datasetA_href.installEventFilter(self)
        self.pushButton_datasetB_href.installEventFilter(self)
        self.pushButton_datasetC_href.installEventFilter(self)

        # Footer Navigation Buttons
        self.pushButton_next.clicked.connect(self.next)

    def eventFilter(self, source, event):
        if source.property("dataset") is not None:
            if event.type() == QEvent.MouseButtonPress:
                if source.isEnabled() is True:
                    # Enable Next button
                    self.pushButton_next.setEnabled(True)

                    # Deselect all datasets
                    for dataset in datasets:
                        if dataset.isEnabled() is False:
                            continue
                        dataset.setProperty("selected", False)
                        dataset.setStyleSheet(dataset.styleSheet())

                    # Select clicked dataset
                    source.setProperty("selected", True)
                    source.setStyleSheet(source.styleSheet())
                    self.selected_dataset = source.property("dataset")
        elif source.property("href-text") is True:
            if event.type() == QEvent.MouseButtonPress:
                popup_window = PopupWindow(self)
                popup_window.show()
                print(source.parent().property("dataset"))
        return super(DatasetWindow, self).eventFilter(source, event)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

