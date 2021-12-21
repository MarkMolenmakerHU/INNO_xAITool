from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Components import Loader, Worker, Modal
from UI.Code.Results import HTMLResult
from UI.Code.Windows import BaseWindow, DatasetWindow, AiModelWindow
from AI_Models.Models.interface_ai_model import InterfaceAiModel
from XAI_Models.Models.lime import LimeXaiModel
from Helpers import load_class, train_ai_model, train_xai_model


class XaiModelWindow(BaseWindow):
    defaults = [
        LimeXaiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget,  dataset_window: DatasetWindow, ai_model_Window: AiModelWindow):
        super().__init__(stackedWidget, 'xai-model')
        self.dataset_window = dataset_window
        self.ai_model_Window = ai_model_Window
        self.loader = Loader(self.nextButton)
        self.worker = Worker(self.train)

    def next(self):

        html = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Home page</title>
                </head>
                <body>
                    <p>
                        This is a simple HTML page.
                    </p>
                </body>
                </html>
                """

        HTMLResult(self, html)

        # self.worker.started.connect(self.loader.start)
        # self.worker.start()
        # self.worker.finished.connect(lambda data: self.on_done(*data))

    def train(self):
        ai_class = load_class('ai_module', self.ai_model_Window.file_name, InterfaceAiModel)
        model, data, names, scores = train_ai_model(ai_class, self.dataset_window.file_name)
        xai_class = LimeXaiModel()
        results = train_xai_model(xai_class, model, data, names)
        return scores, results

    def on_done(self, scores, results):
        self.loader.stop()
        Modal(self, f"Done! (Accuracy: {scores['accuracy']:0.2}, F1: {scores['f1']:0.2}, Results: {results})")
