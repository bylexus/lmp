from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl, QThreadPool, QSettings
from PyQt5 import uic
from classes.log import log
from classes.ui.components.LoadImage import LoadImage
from classes.services.Manager import Manager
from classes.services.ScanDirTask import ScanDirTask
import classes.Application

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
        settings = QSettings()
        prevDir = settings.value('mainwindow/selectsongdir', QUrl())
        filters = map(lambda x: '*'+x,classes.Application.Application.SUPPORTED_EXTENSIONS)
        fileUrl = QFileDialog.getOpenFileUrl(parent = self, caption = "Select Song", filter = "Audio files ({0})".format(filters), directory = str(prevDir))
        if fileUrl:
            log.debug(str(fileUrl[0]))
            settings.setValue('mainwindow/selectsongdir', fileUrl[0])
            return fileUrl[0]
        else:
            return None

    def openSong(self):
        fileName = self.openSelectSongDialog()
        if fileName:
            Manager.mplayer.setPlaylistFromSingleFile(fileName)

    def onScanDirAction(self):
        settings = QSettings()
        prevDir = settings.value('mainwindow/scandir', QUrl())
        scanDir = QFileDialog.getExistingDirectoryUrl(self, "Choose Directory to scan", prevDir)
        if scanDir:
            settings.setValue('mainwindow/scandir', scanDir)
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


