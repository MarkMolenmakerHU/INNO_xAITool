from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QRect
import os


class Loader:
    def __init__(self, parent, auto_start=True):
        label = QLabel(parent)
        
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        label.setSizePolicy(size_policy)
        label.setScaledContents(True)

        directory_path = os.path.dirname(__file__)
        file_path = os.path.join(directory_path, '../../Design/Gifs/spinner.gif')
        self.movie = QMovie(file_path)
        label.setMovie(self.movie)

        if auto_start:
            self.start()

    def start(self):
        self.movie.start()

    def stop(self):
        self.movie.stop()
