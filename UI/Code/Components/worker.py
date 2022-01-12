from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import QThread


class Worker(QObject):
    started = pyqtSignal(bool)
    finished = pyqtSignal(object)

    def __init__(self, job, parent):
        super().__init__(None)
        self.job = job
        self.thread = QThread(parent)
        self.moveToThread(self.thread)
        self.thread.started.connect(self.excute_job)
        
    def start(self):
        self.thread.start()
        print("Started Thread")
        self.started.emit(True)

    def excute_job(self):
        data = self.job()
        self.finished.emit(data)
        print("Finished Thread\n")
