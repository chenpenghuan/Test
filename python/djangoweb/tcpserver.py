from time import sleep
from socketserver import (
    TCPServer as TCP,
    # StreamRequestHandler as SRH,
    ThreadingMixIn as TMI,
    BaseRequestHandler as BRH,
    ThreadingTCPServer as TTCP
)
# 变动位置
# from time import ctime
from urllib.request import urlopen
from json import dumps, loads
from pymysql import connect
HOST = '192.168.1.193'
PORT = 8001
ADDR = (HOST, PORT)


class Server(TMI, TCP):  # 变动位置
    pass


class MyRequestHandler(BRH):
    safeip=['192.168.1.5']
    confsfile = '/home/cph/jsons/cont_conf.json'
    statusfile = '/home/cph/jsons/conf_status.json'
    confs = {}

    def checkconf(self):
        try:
            statusfile = open(self.statusfile)
            status = statusfile.read()
            statusfile.close()
            status = loads(status)
            # print(status)
            if int(status['status']) == 1:
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

    def readconf(self):
        try:
            conn = connect(host='127.0.0.1', user='root', passwd='123123',
                           db='winnerlook', port=3306, charset='utf8')
            cur = conn.cursor()
            sql = 'select id,cont_var,cont_url from cont_conf'
            cur.execute(sql)
            data = cur.fetchall()
        except Exception as err:
            data = 'connection error:' + str(err)
        finally:
            return data

    def writeconf(self, data):
        try:
            for m in data:
                    # db.insert({"id": m[0], "name": m[1], "cont": m[2]})
                    # self.confs[m[0]][m[1]] = m[2]
                self.confs[m[0]] = {'name': m[1], 'cont': m[2]}
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
        for i in self.confs:
            print(str(i)+'=>'+self.confs[str(i)]['name']+'=>'+self.confs[str(i)]['cont'])
            data = urlopen(self.confs[str(i)]['cont']).read().decode('utf-8')
            print(data)
        print(self.client_address)
        if self.client_address[0] in self.safeip:
            print('此IP允许访问')
            sleep(60)
            self.data = self.request.recv(10240)
            self.request.sendall('收到的请求内容是'.encode('utf-8') + self.data)
        else:
            print('此IP不允许访问')
# 变动位置
if __name__=="__main__":
    TCP.allow_reuse_address=True
    tcpServ = TTCP(ADDR, MyRequestHandler)
    print('等待新的连接。。。。')
    tcpServ.serve_forever()

