
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QByteArray
from classes.log import log


class LoadImage(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the file into a QMovie
        movie = QMovie('resources/icons/ajax-loader.gif', QByteArray(), self)

        self.setMovie(movie)
        movie.start()

