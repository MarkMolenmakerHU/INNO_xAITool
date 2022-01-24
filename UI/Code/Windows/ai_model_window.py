from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from AI_Models.Models import SvmAiModel, XgbAiModel
from Helpers import load_ai_model


class AiModelWindow(BaseWindow):
    defaults = [
        SvmAiModel(),
        SvmAiModel(),
        SvmAiModel(),
        XgbAiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'ai-model', 'Python (*.py)')

    def browse_action(self, file_path):
        self.selected_option = load_ai_model(file_path)
