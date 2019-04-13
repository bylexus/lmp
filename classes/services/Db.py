from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import QObject, pyqtSignal, QSettings, QFileInfo, QDir
from classes.log import log

confDir = QFileInfo(QSettings().fileName()).absolutePath()
dbPath = QDir(confDir).absoluteFilePath("lmp.sqlite")

log.debug("SQLITE db is stored here: " + str(dbPath))

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName(dbPath)
if not db.open():
    err = QSqlDatabase.lastError()
    raise SystemError(err)
