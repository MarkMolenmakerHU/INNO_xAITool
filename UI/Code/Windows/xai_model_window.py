from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Components import Loader, Worker, Modal
from UI.Code.Windows import BaseWindow, DatasetWindow, AiModelWindow
from XAI_Models.Models.lime import LimeXaiModel
from Helpers import train_ai_model, train_xai_model


class XaiModelWindow(BaseWindow):
    defaults = [
        LimeXaiModel(),
        LimeXaiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget,  dataset_window: DatasetWindow, ai_model_Window: AiModelWindow):
        super().__init__(stackedWidget, 'xai-model')
        self.dataset_window = dataset_window
        self.ai_model_Window = ai_model_Window
        self.loader = Loader(self.nextButton)
        self.worker = Worker(self.train)

    def next(self):
        self.worker.started.connect(self.loader.start)
        self.worker.start()
        self.worker.finished.connect(lambda data: self.on_done(*data))

    def train(self):
        model, data, names, scores = train_ai_model(self.ai_model_Window.selected_option, self.dataset_window.selected_option)
        results = train_xai_model(self.selected_option, model, data, names)
        return scores, results

    def on_done(self, scores, results):
        self.loader.stop()
        text = f"Done! (Accuracy: {scores['accuracy']:0.2}, F1: {scores['f1']:0.2}, Results: {results})"
        Modal(self, text)
