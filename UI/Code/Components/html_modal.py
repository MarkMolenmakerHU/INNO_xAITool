from typing import List, Optional
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class HtmlModal(QDialog):
    def __init__(self, parent: Optional[QWidget], file_paths: List[str]) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/modal.ui', self)
        self.okButton.clicked.connect(self.close)
        self.setFixedSize(1000, 200 * len(file_paths))
        self.display(file_paths)
        self.show()

    def display(self, file_paths: List[str]):
        for file_path in file_paths:
            webEngineView = QWebEngineView()
            webEngineView.load(QUrl.fromLocalFile(file_path))
            self.layout().insertWidget(0, webEngineView)
