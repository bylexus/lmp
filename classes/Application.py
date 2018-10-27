from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot
from classes.ui.MainWindow import MainWindow
from classes.ui.LogWin import LogWin
from classes.log import log
from classes.services.Manager import Manager

class Application(QApplication):
    def __init__(self, args=[]):
        super().__init__(args)

        self.initUI()

    def initUI(self):
        self.mainWin = MainWindow()
        self.logWin = LogWin(self.mainWin)
        self.logWin.show()
        self.mainWin.show()

        log.debug("Startup completed")

    def setLoading(self, show=False, message=None):
        self.mainWin.setLoading(show, message)

