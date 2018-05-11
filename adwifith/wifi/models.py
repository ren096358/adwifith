import pymysql
from django.db import models


class Model:
    def __init__(self):
        db = pymysql.connect(host="localhost", user="root",
                             passwd="", db="itt_th", charset='utf8')
        self.cursor = db.cursor()
    def getCursor:
        return  cursor


class Hotspotsinfo(Model):
    def __init__(self):
        super().__init__(self)

    def getRid(roterName):
        sql = "select rid from hotspotsinfo where routerName = '%s'" % \
              (roterName)
        self.cursor.execute(sql)

        return self

    def


def get(sql, fetch, action):
    db = pymysql.connect(host="localhost", user="root",
                         passwd="", db="itt_th", charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    if action == 'select':
        if fetch == 'all':
            return cursor.fetchall()
        elif fetch == 'one':
            return cursor.fetchone()
        else:
            return

    elif action == 'insert':
        try:
            db.commit()
        except:
            db.rollback()

            db.close()
