from importlib.machinery import SourceFileLoader
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.uic import loadUi
import sys


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)

        self.browseDataset.clicked.connect(self.browse_dataset)
        self.browseAIModel.clicked.connect(self.browse_aimodel)

        self.buttonConfirm.clicked.connect(self.confirm)
        self.buttonCancel.clicked.connect(self.cancel)

    def browse_dataset(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.pathDataset.setText(fname[0])

    def browse_aimodel(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.pathAIModel.setText(fname[0])

    def confirm(self):
        dataset_path = self.pathDataset.text()
        aimodel_path = self.pathAIModel.text()

        aimodel = SourceFileLoader('aimodel', aimodel_path).load_module()

        aimodel.train_model(dataset_path)

    def cancel(self):
        dataset_path = self.pathDataset.text()
        print(dataset_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())
