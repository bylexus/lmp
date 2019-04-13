from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QSettings
from PyQt5.QtCore import pyqtSlot
from classes.ui.MainWindow import MainWindow
from classes.ui.LogWin import LogWin
from classes.log import log
from classes.services.Manager import Manager
import classes.services.Db
from classes.models.MusicDir import MusicDir

class Application(QApplication):
    SUPPORTED_EXTENSIONS = ['.aac','.mp3', '.m4a','.ogg','.wav']

    def __init__(self, args=[]):
        super().__init__(args)

        # Setup global organization names for storing settings
        QApplication.setOrganizationName('alexi.ch')
        QApplication.setOrganizationDomain('alexi.ch')
        QApplication.setApplicationName('Lexus Music Player')
        QSettings.setDefaultFormat(QSettings.IniFormat)

        self.initApp()
        self.initUI()

    def initApp(self):
        # init Model tables
        MusicDir.checkTable()

    def initUI(self):
        self.mainWin = MainWindow()
        self.logWin = LogWin(self.mainWin)
        self.logWin.show()
        self.mainWin.show()

        log.debug("Startup completed")

    def setLoading(self, show=False, message=None):
        self.mainWin.setLoading(show, message)

