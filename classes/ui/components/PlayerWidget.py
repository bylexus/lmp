from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import Qt
from PyQt5 import uic
from classes.log import log
from classes.services.Manager import Manager


class PlayerWidget (QWidget):

    def __init__(self):
        super().__init__()
        self.state = None
        self.initUI()
        self.updateUIState(Manager.mplayer.state())

    def initUI(self):

        # Load .ui:
        uic.loadUi("ui/PlayerWidget.ui", self)

        self.playBtn.clicked.connect(Manager.mplayer.play)
        self.pauseBtn.clicked.connect(Manager.mplayer.pause)
        self.stopBtn.clicked.connect(Manager.mplayer.stop)

        # progress slider:
        self.sliderIsPressed = False
        self.progressSlider.setMinimum(0)
        self.progressSlider.setMaximum(0)
        self.progressSlider.setTracking(False)
        self.progressSlider.sliderMoved.connect(self.sliderMoved)
        self.progressSlider.sliderPressed.connect(self.sliderStartMove)
        self.progressSlider.sliderReleased.connect(self.sliderEndMove)

        # media player slots connection
        Manager.mplayer.currentMediaChanged.connect(self.mediaChanged)
        Manager.mplayer.mediaStatusChanged.connect(self.mediaStatusChanged)
        Manager.mplayer.stateChanged.connect(self.mediaPlayerStateChanged)
        Manager.mplayer.positionChanged.connect(self.songProgress)
        Manager.mplayer.durationChanged.connect(self.durationUpdated)

    @pyqtSlot(QMediaContent)
    def mediaChanged(self, media):
        log.debug("Media change detected: "+str(media))
        if media:
            self.songLabel.setText(str(media.canonicalUrl().fileName()))
        else:
            self.songLabel.setText("")

    @pyqtSlot(QMediaPlayer.MediaStatus)
    def mediaStatusChanged(self, status):
        log.debug("Media Status change detected: "+str(status))

    @pyqtSlot(QMediaPlayer.State)
    def mediaPlayerStateChanged(self, state):
        log.debug("Media Player state change detected: " + str(state))
        self.updateUIState(state)

    @pyqtSlot("qint64")
    def durationUpdated(self, value):
        self.progressSlider.setMaximum(value);
        self.updateTimeLabel(self.durationLabel, value)

    @pyqtSlot("qint64")
    def songProgress(self, value):
        self.updateTimeLabel(self.positionLabel, value)
        if not self.sliderIsPressed:
            self.progressSlider.setValue(value)

    @pyqtSlot()
    def sliderStartMove(self):
        self.sliderIsPressed = True

    @pyqtSlot(int)
    def sliderMoved(self, value):
        self.updateTimeLabel(self.positionLabel, value)

    @pyqtSlot()
    def sliderEndMove(self):
        log.debug("Slider value: "+str( self.progressSlider.sliderPosition() ))
        Manager.mplayer.setPosition(self.progressSlider.sliderPosition())
        self.sliderIsPressed = False

    def updateTimeLabel(self, label, msValue):
        minute = int(msValue / 1000 / 60)
        second = ( int(msValue / 1000 )) % 60
        label.setText("{0}:{1:0>2}".format(minute, second))

    def updateUIState(self, newState):
        if (newState == self.state):
            return

        self.state = newState

        if (self.state == QMediaPlayer.PausedState):
            self.playBtn.show()
            self.pauseBtn.hide()
            self.stopBtn.setEnabled(True)
        if (self.state == QMediaPlayer.PlayingState):
            self.playBtn.hide()
            self.pauseBtn.show()
            self.stopBtn.setEnabled(True)
        if (self.state == QMediaPlayer.StoppedState):
            self.progressSlider.setValue(0)
            self.updateTimeLabel(self.positionLabel, 0)
            self.playBtn.show()
            self.pauseBtn.hide()
            self.stopBtn.setEnabled(False)

