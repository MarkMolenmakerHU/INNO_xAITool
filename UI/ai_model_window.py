from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi


class AiModelWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget, datasetWindow):
        super(AiModelWindow, self).__init__()
        loadUi('UI/Ui/ai-model.ui', self)
        self.stackedWidget = stackedWidget
        self.datasetWindow = datasetWindow

        # Variables to be used in other windows
        self.selected_aimodel = None

        # AIModel Selection
        global aimodels
        aimodels = [self.widget_aimodelA, self.widget_aimodelB, self.widget_aimodelC]
        for aimodel in aimodels:
            aimodel.installEventFilter(self)

        self.update()

        # AIModel Href
        self.pushButton_aimodelA_href.installEventFilter(self)
        self.pushButton_aimodelB_href.installEventFilter(self)
        self.pushButton_aimodelC_href.installEventFilter(self)

        # Footer Navigation Buttons
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_next.clicked.connect(self.next)

        self.datasetWindow.pushButton_next.clicked.connect(self.update)

    def eventFilter(self, source, event):
        if source.property("aimodel") is not None:
            if event.type() == QEvent.MouseButtonPress:
                if source.isEnabled() is True:
                    # Enable Next button
                    self.pushButton_next.setEnabled(True)

                    # Deselect all aimodels
                    for aimodel in aimodels:
                        if aimodel.isEnabled() is False:
                            continue
                        aimodel.setProperty("selected", False)
                        aimodel.setStyleSheet(aimodel.styleSheet())

                    # Select clicked aimodel
                    source.setProperty("selected", True)
                    source.setStyleSheet(source.styleSheet())
                    self.selected_aimodel = source.property("aimodel")
        elif source.property("href-text") is True:
            if event.type() == QEvent.MouseButtonPress:
                print(source.parent().property("aimodel"))
        return super(AiModelWindow, self).eventFilter(source, event)

    def back(self):
        for aimodel in aimodels:
            aimodel.setEnabled(False)
            aimodel.setProperty("selected", None)
            aimodel.setStyleSheet(aimodel.styleSheet())
        self.selected_aimodel = None
        self.pushButton_next.setEnabled(False)
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def update(self):
        for aimodel in aimodels:
            if self.datasetWindow.selected_dataset not in aimodel.property("allowed-datasets"):
                aimodel.setEnabled(False)
            else:
                aimodel.setEnabled(True)