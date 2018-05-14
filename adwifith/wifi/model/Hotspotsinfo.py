from wifi.models import Model
import pdb


class Hotspotsinfo(Model):
    def __init__(self):
        super(Hotspotsinfo, self).__init__()

    def getRid(self, routerName):
        sql = "select rid from hotspotsinfo where routerName = '%s'" % \
              (routerName)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getUrl(self, rid, page):
        sql = "select " + page + " from forciblyprocess where rid = '%s'" % \
              (rid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getPortalPic(self, rid):
        sql = "select portalPic from portalstyle where rid = '%s'" % \
              (rid)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]

    def getAdvData(self, rid):
        sql = "select * from advdata where rid = '%s'" % \
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
            # 提交到数据库执行
            self._db.commit()
            return True
        except:
            # 如果发生错误则回滚
            self._db.rollback()
            # 关闭数据库连接
            self._db.close()
            return False

    def selectADVR(self, rid, mac):
        sql = "select url from advredirect where rid = '%s' and mac = '%s' order by indexid desc" % \
              (rid, mac)
        self._cursor.execute(sql)
        return self._cursor.fetchone()[0]
