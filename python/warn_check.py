from time import sleep
from urllib import request
from threading import Thread
from redis import Redis

class WarnCheck(object):
    def __init__(self,ip,port,password,confs):
        self.ip=ip
        self.port=port
        self.password=password
        self.confs=confs
        self.conn=Redis(host=self.ip,port=self.port,password=self.password)
    def main(self):
        t = 0
        while t < 100:
            sleep(5)
            for i in self.confs:
                self.conn.publish(i,self.confs[i])
            if t == 99:
                t = 0
            t = t + 1
if __name__ == "__main__":
    confs={'1':'通道拥堵','2':'MAS报错','3':'未知错误'}
    obj=WarnCheck('127.0.0.1',6379,'123123',confs)
    obj.main()
