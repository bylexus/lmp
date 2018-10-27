from PyQt5.QtCore import QObject, pyqtSignal
from time import strftime

class Logger(QObject):

    SEVERITY_DEBUG = 'DEBUG'
    SEVERITY_INFO  = 'INFO'

    debug_logged = pyqtSignal(str, str)
    info_logged = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

    def debug(self, text = "", context = None):
        self.log(Logger.SEVERITY_DEBUG, text, context)

    def info(self, text = "", context = None):
        self.log(Logger.SEVERITY_INFO, text, context)


    def log(self, severity = 'DEBUG', text = "", context = None):
        context = context if context is not None else "DEFAULT"
        now = strftime("%Y-%m-%d %H:%M:%S")
        line = "[{0}] {1} {2}: {3}".format(now, severity, context, text)
        if (severity == Logger.SEVERITY_DEBUG):
            self.debug_logged.emit(line, context)
        if (severity == Logger.SEVERITY_INFO):
            self.info_logged.emit(line, context)
        print(line)

# create single instance, to be used by module consumers
log = Logger()
