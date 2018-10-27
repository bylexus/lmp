from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import QObject, pyqtSignal
from classes.services.MPlayer import MPlayer

class __Manager(QObject):
    def __init__(self):
        super().__init__()
        self._mplayer = None

    @property
    def mplayer(self):
        if not self._mplayer:
            self._mplayer = MPlayer()
        return self._mplayer


Manager = __Manager()
