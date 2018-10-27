from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from classes.ui.MainWindow import MainWindow
from classes.ui.LogWin import LogWin
from classes.log import log
from classes.services.Manager import Manager

import resources.icons

app = QApplication([])


mainWin = MainWindow()
logWin = LogWin(mainWin)
logWin.show()
mainWin.show()

log.debug("Startup completed")

log.debug("Media status: "+str(Manager.mplayer.mediaStatus()))

fileName = mainWin.openSelectSongDialog()
if fileName:
    Manager.mplayer.setPlaylistFromSingleFile(QUrl.fromLocalFile(fileName))

app.exec_()
