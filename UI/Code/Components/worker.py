from PyQt5.QtCore import QObject, pyqtSignal


class Worker(QObject):
    done = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

    def doWork(self, job):
        print("Start")
        job()
        self.done.emit(True)
        print("done")


# self.thread = QThread(self)
# self.worker = Worker()
# self.worker.moveToThread(self.thread) # worker will be runned in another thread
# self.worker.done.connect(lambda: print("test")) # Call load_data_to_tree when worker.done is emitted
# self.thread.started.connect(self.worker.doWork) # Call worker.doWork when the thread starts
# self.thread.start() # Start the thread (and run doWork)
