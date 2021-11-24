from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget
from PyQt5.uic import loadUi


class AiModelWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget):
        super(AiModelWindow, self).__init__()
        loadUi('UI/Ui/ai-model.ui', self)
        self.stackedWidget = stackedWidget

        # Variables to be used in other windows
        self.selected_aimodel = None

        # AIModel Selection
        global aimodels
        aimodels = [self.widget_aimodelA, self.widget_aimodelB, self.widget_aimodelC]
        for aimodel in aimodels:
            aimodel.installEventFilter(self)

        # AIModel Href
        self.pushButton_aimodelA_href.installEventFilter(self)
        self.pushButton_aimodelB_href.installEventFilter(self)
        self.pushButton_aimodelC_href.installEventFilter(self)

        # Footer Navigation Buttons
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_next.clicked.connect(self.next)

    def eventFilter(self, source, event):
        if source.property("aimodel") is not None:
            if event.type() == QEvent.MouseButtonPress:
                if source.isEnabled() is True:
                    # Enable Next button
                    self.pushButton_next.setEnabled(True)

                    # Deselect all datasets
                    for aimodel in aimodels:
                        if aimodel.isEnabled() is False:
                            continue
                        aimodel.setProperty("selected", False)
                        aimodel.setStyleSheet(aimodel.styleSheet())

                    # Select clicked dataset
                    source.setProperty("selected", True)
                    source.setStyleSheet(source.styleSheet())
                    self.selected_aimodel = source.property("aimodel")
        elif source.property("href-text") is True:
            if event.type() == QEvent.MouseButtonPress:
                print(source.parent().property("dataset"))
        return super(AiModelWindow, self).eventFilter(source, event)

    def back(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
