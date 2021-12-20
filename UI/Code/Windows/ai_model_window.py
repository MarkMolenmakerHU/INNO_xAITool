from PyQt5.QtWidgets import QStackedWidget
from UI.Code.Windows.base_window import BaseWindow


class AiModelWindow(BaseWindow):
    defaults = [
        "D:/Documents/School/Hogeschool/Leerjaar 3/Blok 2/Innovation (INNO)/INNO_xAITool/AI_Models/Models/iris_ai_model.py",
        "D:/Documents/School/Hogeschool/Leerjaar 3/Blok 2/Innovation (INNO)/INNO_xAITool/AI_Models/Models/iris_ai_model.py",
    ]

    def __init__(self, stackedWidget: QStackedWidget):
        super().__init__(stackedWidget, 'ai-model')
