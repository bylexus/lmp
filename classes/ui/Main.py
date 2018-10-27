from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.Qt import Qt
from classes.log import log
from classes.ui.components.PlayerWidget import PlayerWidget


class Main (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello, World!")

        fileMenu = self.menuBar().addMenu("&File")

        closeAction = fileMenu.addAction("Shutdown")
        closeAction.setShortcut(Qt.CTRL + Qt.Key_S)
        closeAction.setStatusTip("Exit application")
        closeAction.triggered.connect(QApplication.quit)

        playerWidget = PlayerWidget()
        self.setCentralWidget(playerWidget)

        self.statusBar().showMessage("Ready")

    def openSelectSongDialog(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Song", None, "Audio files (*.mp3 *.m4a *.ogg *.wav)")
        log.info("File chosen: "+fileName[0])
        if fileName:
            return fileName[0]
        else:
            return None

