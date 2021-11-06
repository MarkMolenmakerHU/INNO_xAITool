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
        # Store the selected paths in variables
        dataset_path = self.pathDataset.text()
        aimodel_path = self.pathAIModel.text()

        # Read the .py file
        with open(aimodel_path) as r:
            lines = r.readlines()

        # Write code into the .py file
        # @TODO: Kopie maken van file in runtime
        # @TODO: kopie aanpassen (code injecteren)
        # @TODO: kopie uitvoeren
        # @TODO: kopie weggooien na sluiten van tool
        # @TODO: TLDR: Find a way to modify a .py file, while not overwriting the original file

        # Load the .py file from the path
        aimodel = SourceFileLoader('aimodel', aimodel_path).load_module()


        # Execute the .py file method with the dataset path
        aimodel.train_model(dataset_path)

    def cancel(self):
        dataset_path = self.pathDataset.text()
        print(dataset_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())
