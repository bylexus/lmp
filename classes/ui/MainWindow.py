from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl, QThreadPool
from PyQt5 import uic
from classes.log import log
from classes.ui.components.LoadImage import LoadImage
from classes.services.Manager import Manager
from classes.services.ScanDirTask import ScanDirTask

class MainWindow (QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Load .ui:
        uic.loadUi("ui/MainWindow.ui", self)

        self.setWindowTitle("Hello, World!")

        self.__loadImg = LoadImage()
        self.setLoading(False)
        self.statusbar.addPermanentWidget(self.__loadImg)

        self.actionOpen.triggered.connect(self.openSong)
        self.actionScanDir.triggered.connect(self.onScanDirAction)

    def openSelectSongDialog(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Song", None, "Audio files (*.aac *.mp3 *.m4a *.ogg *.wav)")
        log.info("File chosen: "+fileName[0])
        if fileName:
            return fileName[0]
        else:
            return None

    def openSong(self):
        fileName = self.openSelectSongDialog()
        if fileName:
            Manager.mplayer.setPlaylistFromSingleFile(QUrl.fromLocalFile(fileName))

    def onScanDirAction(self):
        scanDir = QFileDialog.getExistingDirectoryUrl(self, "Choose Directory to scan")
        if scanDir:
            QApplication.instance().setLoading(True, "Scan directory " + str(scanDir))

            task = ScanDirTask(scanDir)
            task.signals.finished.connect(QApplication.instance().setLoading)
            QThreadPool.globalInstance().start(task)


    def setLoading(self, show=False, message=None):
        self.__loadImg.setVisible(show)
        if show and message:
            self.statusbar.showMessage(message)
        else:
            self.statusbar.clearMessage()


