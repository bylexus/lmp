from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.Qt import Qt
from PyQt5 import uic
from classes.log import log


class MainWindow (QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Load .ui:
        uic.loadUi("ui/MainWindow.ui", self)

        self.setWindowTitle("Hello, World!")

        # fileMenu = self.menuBar().addMenu("&File")

        # closeAction = fileMenu.addAction("Shutdown")
        # closeAction.setShortcut(Qt.CTRL + Qt.Key_S)
        # closeAction.setStatusTip("Exit application")
        # closeAction.triggered.connect(QApplication.quit)

        # playerWidget = PlayerWidget()
        # self.setCentralWidget(playerWidget)
        #
        # self.statusBar().showMessage("Ready")

    def openSelectSongDialog(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Song", None, "Audio files (*.mp3 *.m4a *.ogg *.wav)")
        log.info("File chosen: "+fileName[0])
        if fileName:
            return fileName[0]
        else:
            return None
