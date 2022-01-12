import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from UI.Code.Windows import DatasetWindow, AiModelWindow, XaiModelWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    dataset_window = DatasetWindow(stacked_widget)
    ai_model_window = AiModelWindow(stacked_widget)
    xai_model_window = XaiModelWindow(stacked_widget, dataset_window, ai_model_window)
    [stacked_widget.addWidget(window) for window in [dataset_window, ai_model_window, xai_model_window]]
    stacked_widget.show()

    sys.exit(app.exec_())
