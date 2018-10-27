from PyQt5.QtCore import QObject,QRunnable,QThread, pyqtSignal, pyqtSlot
from classes.log import log
import time

class Signals(QObject):
    finished = pyqtSignal()

class ScanDirTask(QRunnable):

    def __init__(self, url):
        super().__init__()
        self.dirUrl = url
        self.signals = Signals()


    @pyqtSlot()
    def run(self):
        log.debug("Scanning dir: "+str(self.dirUrl))
        QThread.sleep(2)
        self.signals.finished.emit()

