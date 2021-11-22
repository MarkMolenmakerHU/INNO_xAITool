from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QSize
import os


class Loader:
    def __init__(self, parent):
        self.wrapper = [parent]
        self.parent.setIconSize(QSize(50, 50))

        directory_path = os.path.dirname(__file__)
        file_path = os.path.join(directory_path, '../../Design/Gifs/spinner.gif')
        self.movie = QMovie(file_path)

    @property
    def parent(self):
        return self.wrapper[0]

    @property
    def icon(self):
        return QIcon(self.movie.currentPixmap())
    
    def start(self):
        self.movie.start()
        self.update(self.icon, False)
        self.movie.frameChanged.connect(lambda: self.parent.setIcon(self.icon))

    def stop(self):
        self.movie.stop()
        self.update(QIcon(), True)

    def update(self, icon, enabled):
        self.parent.setIcon(icon)
        self.parent.update()
        self.parent.setEnabled(enabled)
