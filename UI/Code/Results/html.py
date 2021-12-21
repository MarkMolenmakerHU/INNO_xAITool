from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from typing import Optional


class HTMLResult(QDialog):
    def __init__(self, parent: Optional[QWidget], html: str) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/Results/html.ui', self)
        self.okButton.clicked.connect(self.close)

        self.webEngineView = QWebEngineView()
        self.webEngineView.setHtml(html)
        self.layout.addWidget(self.webEngineView)

        self.show()
