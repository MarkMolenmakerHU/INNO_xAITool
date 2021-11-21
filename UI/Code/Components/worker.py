from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import QThread

class Worker(QObject):
    started = pyqtSignal(bool)
    finished = pyqtSignal(bool)

    def __init__(self, job):
        super().__init__(None)
        self.job = job

        self.thread = QThread()
        self.moveToThread(self.thread)
        
        # self.finished.connect(self.thread.quit)
        # self.finished.connect(self.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)

        self.thread.started.connect(self.do)
        
    def start(self):
        self.thread.start()

    def do(self):
        print("Started Thread")
        self.started.emit(True)
        self.job()
        self.finished.emit(True)
        print("Finished Thread")
