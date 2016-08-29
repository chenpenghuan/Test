from tinydb import TinyDB, where
from pymysql import *


def select(sql):
    try:
        conn = connect(
            host='192.168.1.198',
            user='root',
            passwd='123123',
            db='cleanpt',
            port=3306,
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
    except Exception as err:
        data = 'connection error:' + str(err)
    finally:
        return data
sql = 'select num,code from status where iftrust=1 limit 10000'
result = select(sql)
db = TinyDB('/home/cph/tinydb/status.json')
for m, n in result:
    db.insert({'num': m, 'code': n})
db.close()
