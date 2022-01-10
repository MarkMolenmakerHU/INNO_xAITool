from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from AI_Models.Models.svm_ai_model import SvmAiModel


class AiModelWindow(BaseWindow):
    defaults = [
        SvmAiModel(),
        SvmAiModel(),
        SvmAiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'ai-model')
