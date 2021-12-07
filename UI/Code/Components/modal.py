from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from typing import Optional


class Modal(QDialog):
    def __init__(self, parent: Optional[QWidget], text: str) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/modal.ui', self)
        self.okButton.clicked.connect(self.close)
        self.textBrowser.setText(text)
        self.show()
