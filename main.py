from PyQt5.QtWidgets import QApplication, QStackedWidget
from UI.Code.dataset_window import DatasetWindow
from UI.Code.ai_model_window import AiModelWindow
from UI.Code.xai_model_window import XaiModelWindow
import sys
from PyQt5.QtCore import Qt


if __name__ == '__main__':
    app = QApplication(sys.argv)

    stackedWidget = QStackedWidget()
    datasetWindow = DatasetWindow(stackedWidget)
    aiModelWindow = AiModelWindow(stackedWidget, datasetWindow)
    xaiModelWindow = XaiModelWindow(stackedWidget, datasetWindow, aiModelWindow)
    [stackedWidget.addWidget(window) for window in [datasetWindow, aiModelWindow, xaiModelWindow]]
    stackedWidget.show()
    
    sys.exit(app.exec_())
