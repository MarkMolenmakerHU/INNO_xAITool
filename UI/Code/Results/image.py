from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget, QLabel
from PyQt5.QtCore import Qt, QUrl
from typing import Optional


class ImageResult(QDialog):
    def __init__(self, parent: Optional[QWidget], title: str, path: str) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/Results/dialog.ui', self)
        self.okButton.clicked.connect(self.close)

        self.setWindowTitle(title)

        self.imageLabel = QLabel()
        pixmap = QPixmap(path)
        self.imageLabel.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.layout.addWidget(self.imageLabel)

        self.show()
