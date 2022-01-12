from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Components import Loader, Worker, Modal
from UI.Code.Windows import BaseWindow, DatasetWindow, AiModelWindow
from Helpers import train_ai_model, train_xai_model
from XAI_Models.Models import LimeXaiModel, ShapXaiModel


class XaiModelWindow(BaseWindow):
    defaults = [
        LimeXaiModel(),
        ShapXaiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget,  dataset_window: DatasetWindow, ai_model_Window: AiModelWindow):
        super().__init__(stackedWidget, 'xai-model')
        self.dataset_window = dataset_window
        self.ai_model_Window = ai_model_Window
        self.loader = Loader(self.nextButton)

    def next(self):
        self.worker = Worker(self.train, self)
        self.worker.started.connect(self.loader.start)
        self.worker.finished.connect(lambda data: self.on_done(*data))
        self.worker.start()

    def train(self):
        model, data, names, scores = train_ai_model(self.ai_model_Window.selected_option, self.dataset_window.selected_option)
        results = train_xai_model(self.selected_option, model, data, names)
        return scores, results

    def on_done(self, scores, results):
        self.loader.stop()
        text = f"Done! (Accuracy: {scores['accuracy']:0.2}, F1: {scores['f1']:0.2}, Results: {results})\n"
        text += f"With dataset: {self.dataset_window.selected_option['filename']}\n"
        text += f"Ai-model: {type(self.ai_model_Window.selected_option).__name__}\n"
        text += f"Xai-model: {type(self.selected_option).__name__}\n"
        Modal(self, text)
