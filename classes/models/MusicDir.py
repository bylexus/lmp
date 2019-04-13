from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery



class MusicDir(QSqlTableModel):
    def checkTable():
        query = QSqlQuery("CREATE TABLE IF NOT EXISTS music_dir (path TEXT, last_synced TEXT)", QSqlDatabase.database())
        if not query.exec():
            raise Exception(query.lastError())


    def __init__(self, parent = None, db = None):
        super().__init__(parent, db)


