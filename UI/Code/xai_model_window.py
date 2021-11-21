from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from Helpers.class_helper import load_class
from Helpers.model_helper import train_model
from AI_Models.Models.interface_ai_model import InterfaceAiModel
from UI.Code.Components.worker import Worker
from UI.Code.Components.loader import Loader


class XaiModelWindow(QMainWindow):
    def __init__(self, stackedWidget: QStackedWidget, datasetWindow, aiModelWindow):
        super(XaiModelWindow, self).__init__()
        loadUi('UI/Design/xai-model.ui', self)
        
        self.stackedWidget = stackedWidget
        self.datasetWindow = datasetWindow
        self.aiModelWindow = aiModelWindow
        
        self.prevButton.clicked.connect(self.prev)
        self.nextButton.clicked.connect(self.next)

        self.loader = Loader(self.nextButton)
        self.worker = Worker(self.train)

    def prev(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    def next(self):
        self.worker.started.connect(self.loader.start)
        self.worker.start()
        self.worker.finished.connect(self.loader.stop)

    def train(self):
        ai_class = load_class('ai_module', self.aiModelWindow.file_name, InterfaceAiModel)
        accuracy, f1 = train_model(ai_class, self.datasetWindow.file_name)
        print(f'Done! (Accuracy: {accuracy:0.2}, F1: {f1:0.2})')

