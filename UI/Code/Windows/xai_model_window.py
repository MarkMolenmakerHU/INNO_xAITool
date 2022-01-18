from PyQt5.QtWidgets import QStackedWidget, QFileDialog
from UI.Code.Components import Loader, Worker, TextModal
from UI.Code.Components.html_modal import HtmlModal
from UI.Code.Windows import BaseWindow, DatasetWindow, AiModelWindow
from Helpers import train_ai_model, train_xai_model, get_combination_names, get_file_name
from XAI_Models.Models import LimeXaiModel, ShapXaiModel


class XaiModelWindow(BaseWindow):
    defaults = [
        LimeXaiModel(),
        ShapXaiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget,  dataset_window: DatasetWindow, ai_model_Window: AiModelWindow):
        super().__init__(stackedWidget, 'xai-model')
        self.displayButton.clicked.connect(self.display)
        self.dataset_window = dataset_window
        self.ai_model_Window = ai_model_Window
        self.loader = Loader(self.nextButton)

    def next(self):
        self.worker = Worker(self.train, self)
        self.worker.started.connect(self.loader.start)
        self.worker.finished.connect(lambda data: self.on_done(*data))
        self.worker.start()

    def train(self):
        file_name = get_file_name(*self.selected_options)
        model, data, names, scores = train_ai_model(self.ai_model_Window.selected_option, self.dataset_window.selected_option)
        results = train_xai_model(self.selected_option, model, data, names, file_name)
        return scores, results

    def display(self):
        file_paths = QFileDialog.getOpenFileNames(self, 'Open file', './Results')[0]
        HtmlModal(self, file_paths)

    def on_done(self, scores, results):
        self.loader.stop()
        dataset_name, ai_model_name, xai_model_name = get_combination_names(*self.selected_options)
        text = f"Done! (Accuracy: {scores['accuracy']:0.2}, F1: {scores['f1']:0.2}, Results: {results})\n"
        text += f"With dataset: {dataset_name}\n"
        text += f"Ai-model: {ai_model_name}\n"
        text += f"Xai-model: {xai_model_name}\n"
        TextModal(self, text)

    @property
    def selected_options(self):
        return self.dataset_window.selected_option, self.ai_model_Window.selected_option, self.selected_option
