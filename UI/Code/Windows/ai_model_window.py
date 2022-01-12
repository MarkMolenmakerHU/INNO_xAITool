from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow
from AI_Models.Models import SvmAiModel, XgbAiModel


class AiModelWindow(BaseWindow):
    defaults = [
        SvmAiModel(),
        SvmAiModel(),
        SvmAiModel(),
        XgbAiModel()
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'ai-model')
