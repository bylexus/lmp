from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from classes.log import log


class LogWin (QDialog):

    textarea = None

    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Log Output")
        self.resize(700,150)

        layout = QVBoxLayout()

        self.textarea = QTextEdit()
        self.textarea.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.textarea)
        log.debug_logged.connect(self.debug_logged)
        log.info_logged.connect(self.debug_logged)

        self.setLayout(layout)

    @pyqtSlot(str, str)
    def debug_logged(self, text, context):
        if self.textarea is not None:
            self.textarea.append(text)


