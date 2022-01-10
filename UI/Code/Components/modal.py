from io import TextIOWrapper
from typing import Optional

from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTextBrowser, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Modal(QDialog):
    def __init__(self, parent: Optional[QWidget], content: str or TextIOWrapper) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/modal.ui', self)
        self.okButton.clicked.connect(self.close)
        display_conent = self.display_html if type(content) == TextIOWrapper else self.display_text
        display_conent(content)
        self.show()

    def display_text(self, text: str):
        textBrowser = QTextBrowser()
        font = QFont()
        font.setPixelSize(12)
        textBrowser.setText(text)
        textBrowser.setFont(font)
        self.layout().insertWidget(0, textBrowser)

    def display_html(self, html_file: TextIOWrapper):
        webEngineView = QWebEngineView()
        webEngineView.setHtml(html_file.read())
        self.layout().insertWidget(0, webEngineView)
