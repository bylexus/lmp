from PyQt5.QtCore import QObject,QRunnable,QThread, pyqtSignal, pyqtSlot
from classes.log import log
import time
import os
import classes.Application
import mutagen

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
        self.processDir(self.dirUrl)
        self.signals.finished.emit()

    def processDir(self, dirUrl):
        for root, dirs, files in os.walk(dirUrl.path()):
            for fileName in files:
                fullPath = os.path.join(root, fileName)
                name, ext = os.path.splitext(fullPath)
                if ext.lower() in classes.Application.Application.SUPPORTED_EXTENSIONS:
                    info = mutagen.File(fullPath)
                    if info:
                        self.processFileInfo(fullPath, info)

    def processFileInfo(self,fullPath, mutagenFileInfo):
        tags = mutagenFileInfo.tags
        info = mutagenFileInfo.info
        log.debug("{0}: {1}, {2}s".format(fullPath,type(mutagenFileInfo), info.length))
        log.debug(mutagenFileInfo.keys())
