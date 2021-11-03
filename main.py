from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.uic import loadUi
import sys


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)

        self.browseDataset.clicked.connect(self.browse_dataset)
        self.browseAIModel.clicked.connect(self.browse_aimodel)

    def browse_dataset(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/')
        self.pathDataset.setText(fname[0])

    def browse_aimodel(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/')
        self.pathAIModel.setText(fname[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())
