from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from Helpers.class_helper import load_class
from AI_Models.interface_ai_model import InterfaceAiModel


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
        ai_class = load_class('ai_model', self.aiModelWindow.file_name, InterfaceAiModel)
        accuracy, f1 = ai_class.train_model(self.datasetWindow.file_name)
        print(f'Accuracy: {accuracy:0.2}, F1: {f1:0.2}')
