from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtGui import QMovie
import os


class Loader:
    def __init__(self, parent):
        self.parent = parent

        self.label = QLabel(self.parent)
        self.label.setScaledContents(True)

        self.hl = QHBoxLayout(self.parent)
        self.hl.addWidget(self.label)
        
        directory_path = os.path.dirname(__file__)
        file_path = os.path.join(directory_path, '../../Design/Gifs/spinner.gif')
        self.movie = QMovie(file_path)

    def start(self):
        self.movie.start()
        self.update(self.movie, False)

    def stop(self):
        self.movie.stop()
        self.update(None, True)

    def update(self, movie, enabled):
        self.label.setMovie(movie)
        self.label.update()
        self.parent.setEnabled(enabled)
