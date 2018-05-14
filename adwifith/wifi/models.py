import pymysql


class Model(object):

    def __init__(self):
        db_host = "localhost"
        db_user = "root"
        db_password = ""
        db_name = "itt_th"

        self._db = pymysql.connect(db_host, db_user, db_password, db_name, charset="utf8", port=3306)
        self._cursor = self._db.cursor()
