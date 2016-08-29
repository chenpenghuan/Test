#!/usr/bin/env Python3
from os import popen, system
from sys import exc_info
from time import sleep, strftime

while True:
    sleep(4)
    #ret = os.popen('ps -C apache -o pid,cmd').readlines()
    try:
        ret = popen('pgrep apache2').readlines()
        if len(ret) < 2:
            print(strftime("%Y-%m-%d %H:%M:%S")+"\tapache 进程异常退出， 4 秒后重新启动")
            sleep(3)
            system(strftime("%Y-%m-%d %H:%M:%S")+"\tservice apache2 restart")
        else:
            print(strftime("%Y-%m-%d %H:%M:%S")+"\tapache 进程正常运行")
    except:
        print(strftime("%Y-%m-%d %H:%M:%S")+"\tError", exc_info()[1])
