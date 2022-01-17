from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt, QUrl
from typing import Optional


class HTMLResult(QDialog):
    def __init__(self, parent: Optional[QWidget], title: str, path: str) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/Results/dialog.ui', self)
        self.okButton.clicked.connect(self.close)

        self.setWindowTitle(title)

        self.webEngineView = QWebEngineView()
        self.webEngineView.load(QUrl.fromLocalFile(path))

        self.layout.addWidget(self.webEngineView)

        self.show()
