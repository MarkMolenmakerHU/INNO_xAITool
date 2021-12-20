from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import QThread


class Worker(QObject):
    started = pyqtSignal(bool)
    finished = pyqtSignal(object)

    def __init__(self, job):
        super().__init__(None)
        self.job = job
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.do)
        
    def start(self):
        self.thread.start()

    def do(self):
        print("Started Thread")
        self.started.emit(True)
        data = self.job()
        self.finished.emit(data)
        print("Finished Thread")
