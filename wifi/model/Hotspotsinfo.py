from wifi.models import Model
import pdb


class Hotspotsinfo(Model):
    def __init__(self):
        super(Hotspotsinfo, self).__init__()

    def getRid(self, routerName):
        sql = "SELECT rid FROM hotspotsinfo WHERE routerName = '%s'" % \
              (routerName)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getUrl(self, rid, page):
        sql = "SELECT " + page + " FROM forciblyprocess WHERE rid = '%s'" % \
              (rid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getPortalPic(self, rid):
        sql = "SELECT portalPic FROM portalstyle WHERE rid = '%s'" % \
              (rid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getAdvData(self, rid):
        sql = "SELECT * FROM advdata WHERE rid = '%s'" % \
              (rid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def getAdvUrl(self, rid, mac):
        url = self.getUrl(rid, "advinner")
        advData = self.getAdvData(rid)
        url += "?ad_rid=%d&ad_mac=%s&ad_type=%s&ad_key=%s&ad_nums=%d&ad_defaultId=%d&ad_specifyId=%d" \
               % (advData[0], mac, advData[2], advData[1], advData[3], advData[4], advData[5])
        return url

    def insertADVR(self, rid, mac, url):
        sql = "INSERT INTO advredirect (rid, url, mac) VALUES ('%s', '%s', '%s')" % \
              (rid, url, mac)
        self._cursor.execute(sql)
        try:
            self._db.commit()
            return True
        except:
            self._db.rollback()
            self._db.close()
            return False

    def selectADVR(self, rid, mac):
        sql = "SELECT url FROM advredirect WHERE rid = '%s' AND mac = '%s' ORDER BY indexid DESC LIMIT 1" % \
              (rid, mac)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]
