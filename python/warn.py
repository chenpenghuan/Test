#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-01 15:55:56
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urllib.request import urlopen
from json import dumps, loads
from pymysql import connect
from os import path


class Warn(object):

    def __init__(self, confs, confsfile, statusfile):
        self.confs = confs
        self.confsfile = confsfile
        self.statusfile = statusfile

    def checkconf(self):
        try:
            statusfile = open(self.statusfile)
            status = statusfile.read()
            statusfile.close()
            status = loads(status)
            # print(status)
            if int(status['status']) == 1 or not path.isfile(self.confsfile):
                status = True
                statusfile = open(self.statusfile, 'w')
                statusfile.write(dumps({'status': 0}))
                statusfile.close()
            else:
                status = False
        except Exception:
            status = True
        finally:
            return status

    def insert(self, sql):
        try:
            conn = connect(
                host='127.0.0.1',
                user='root',
                passwd='123123',
                db='winnerlook',
                port=3306,
                charset='utf8')
            cur = conn.cursor()
            cur.execute(sql)
            result = True
        except Exception:
            result = False
        finally:
            conn.commit()
            cur.close()
            conn.close()
            return result

    def readconf(self):
        try:
            conn = connect(
                host='127.0.0.1',
                user='root',
                passwd='123123',
                db='winnerlook',
                port=3306,
                charset='utf8')
            cur = conn.cursor()
            # sql = 'select cont_conf.item_id,contents.id,cont_conf.cont_var,cont_conf.cont_url,cont_conf.cont_sec,contents.cont_text,contents.update_sec from cont_conf left join contents on cont_conf.id=contents.cont_id order by item_id,cont_sec'
            sql = 'select item_id,id,cont_var,cont_url,cont_sec,cont_title from cont_conf'
            cur.execute(sql)
            data = cur.fetchall()
        except Exception as err:
            data = 'connection error:' + str(err)
        finally:
            conn.commit()
            cur.close()
            conn.close()
            return data

    def writeconf(self, data):
        try:
            for m in data:
                    # db.insert({"id": m[0], "name": m[1], "cont": m[2]})
                    # self.confs[m[0]][m[1]] = m[2]
                if self.confs.get(m[0]) is None:
                    self.confs[m[0]] = {}
                self.confs[
                    m[0]][
                    m[1]] = {
                    "cont_var": m[2],
                    "cont_url": m[3],
                    "cont_sec": m[4]}
            confsfile = open(self.confsfile, 'w', encoding='utf-8')
            confsfile.write(dumps(self.confs))
            confsfile.close()
            result = True
        except Exception:
            result = False
        finally:
            return result

    def handle(self):
        if self.checkconf():
            data = self.readconf()
            self.writeconf(data)
        else:
            confsfile = open(self.confsfile)
            self.confs = loads(confsfile.read())
            confsfile.close()
        print(data)

if __name__ == "__main__":
    #safeip = ['192.168.1.5', '192.168.168.130']
    confsfile = '/home/cph/jsons/cont_conf.json'
    statusfile = '/home/cph/jsons/conf_status.json'
    confs = {}
    #mon = Warn(safeip, confsfile, statusfile, confs)
    mon = Warn(confsfile, statusfile, confs)
    mon.handle()
