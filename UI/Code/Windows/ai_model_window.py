from PyQt5.QtWidgets import QStackedWidget
from AI_Models.Models.interface_ai_model import InterfaceAiModel
from UI.Code.Windows.base_window import BaseWindow
from AI_Models.Models import DtAiModel, LrAiModel, SvmAiModel, XgbAiModel
from Helpers import load_class


class AiModelWindow(BaseWindow):
    defaults = [
        DtAiModel(),
        LrAiModel(),
        SvmAiModel(),
        XgbAiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'ai-model', 'Python (*.py)', 'AI_Models/Models')

    def browse_action(self, file_path):
        self.selected_option = load_class('ai_module', file_path, InterfaceAiModel)
