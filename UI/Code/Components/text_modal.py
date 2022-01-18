from typing import Optional
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QTextBrowser, QWidget
from PyQt5.QtCore import Qt


class TextModal(QDialog):
    def __init__(self, parent: Optional[QWidget], content: str) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/modal.ui', self)
        self.okButton.clicked.connect(self.close)
        self.display(content)
        self.show()

    def display(self, text: str):
        textBrowser = QTextBrowser()
        font = QFont()
        font.setPixelSize(12)
        textBrowser.setText(text)
        textBrowser.setFont(font)
        self.layout().insertWidget(0, textBrowser)
