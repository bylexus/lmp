from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QObject, pyqtSignal, QUrl

class MPlayer(QMediaPlayer):
    def __init__(self):
        super().__init__()

    """
    @param url: QUrl
    """
    def setMediaFromUrl(self, url):
        self.setMedia(QMediaContent(url))

    """
    @param url: QUrl
    """
    def setPlaylistFromSingleFile(self, url):
        lst = QMediaPlaylist(self)
        lst.addMedia(QMediaContent(url))
        lst.setPlaybackMode(QMediaPlaylist.Loop)
        self.setPlaylist(lst)


