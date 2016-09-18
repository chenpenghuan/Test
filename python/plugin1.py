from redis import Redis
from urllib import request
from json import loads, dumps
from pymysql import connect
from time import time,localtime,strftime

class Recieve(object):

    def __init__(self, ip, port, password, confs, subcha):
        self.ip = ip
        self.port = port
        self.password = password
        self.confs = confs
        self.subcha = subcha
        self.conn = Redis(host=self.ip, port=self.port, password=self.password)

    def main(self):
        sub = self.conn.pubsub()
        sub.subscribe(self.subcha)
        for msg in sub.listen():
            if msg['type'] == 'message':
                # print(msg['channel'].decode('utf-8'))
                jsonstr = request.urlopen(
                    'http://localhost/test.php').read().decode('utf-8')
                # print(loads(jsonstr)['warn_cont'])
                conts = loads(jsonstr)
                # print(conts)
                if conts['warn_true'] == 'true':
                    sql = 'insert into warn_cont(warn_id,warn_cont,warn_date) values(' + msg[
                        'channel'].decode('utf-8') + ',"' + conts['warn_cont'] + '","'+strftime("%Y-%m-%d %H:%M:%S",localtime(time()))+'")'
                mydb=connect(host='127.0.0.1',user='root',password='123123',db='winnerlook',port=3306,charset='utf8')
                cur=mydb.cursor()
                cur.execute(sql)
                mydb.commit()
                cur.close()
                mydb.close()

if __name__ == "__main__":
    confs = {'1': '通道拥堵', '2': 'MAS报错', '3': '未知错误'}
    subcha = ['1']
    obj = Recieve('127.0.0.1', 6379, '123123', confs, subcha)
    obj.main()
