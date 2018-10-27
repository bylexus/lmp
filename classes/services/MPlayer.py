from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QObject, pyqtSignal, QUrl

class MPlayer(QMediaPlayer):
    def __init__(self):
        super().__init__()

    def setMediaFromUrl(self, url):
        if not isinstance(url, QUrl):
            url = QUrl.fromLocalFile(url)
        self.setMedia(QMediaContent(url))

    def setPlaylistFromSingleFile(self, url):
        if not isinstance(url, QUrl):
            url = QUrl.fromLocalFile(url)
        lst = QMediaPlaylist(self)
        lst.addMedia(QMediaContent(url))
        lst.setPlaybackMode(QMediaPlaylist.Loop)
        self.setPlaylist(lst)


