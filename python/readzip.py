import zipfile
import os
import glob
import codecs
import csv
from pymysql import *
from time import *


def select(sql):
    conn = connect(
        host='localhost',
        user='root',
        passwd='123123',
        db='cleanpt',
        port=3306,
        charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data


def update(sql):
    conn = connect(
        host='localhost',
        user='root',
        passwd='123123',
        db='cleanpt',
        port=3306,
        charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)


def scan_mysql():
    global conn
    conn = connect(
        host='localhost',
        user='root',
        passwd='123123',
        db='test',
        port=3306,
        charset='utf8')
    global cur
    cur = conn.cursor()
    findtask(3)
    cur.close()
    conn.close()


def findtask(waittime):
    sleep(waittime)
    cur.execute('select taskid,username,tasktime,taskcode,upload,download,tasklevel,taskstatus from taskinfo where taskstatus=0 order by tasklevel limit 1')
    data = cur.fetchall()
    if(len(data) > 0):
        print('发现任务，信息如下，交给大数据平台处理')
        print(str(data[0][4]))
        if update(
                'update takinfo set taskstatus=1 where taskid=' + data[0][0]):
            print('大数据平台开始处理')
        else:
            print('大数据平台接受任务出错')
        flag = input('大数据平台处理结束，返回信号')
        if flag:
            print('大数据处理完了，查找下一个任务')
            findtask(waittime)
# scan_mysql()


def readzip(zfile='test.zip', zpath='E:',
            topath='E:\\temp', logpath='E:\\log'):
    if os.path.exists(logpath):
        print('日志文件夹存在，继续后续操作')
    else:
        print('日志文件夹不存在，马上创建')
        os.mkdir(logpath)
    logfile = open(logpath + '\\' + 'readme.log', 'a', encoding='UTF-8')
    infofile = open(topath + '\\' + 'readme.txt', 'a', encoding='UTF-8')
    if os.path.exists(zpath + '//' + zfile):
        print('压缩文件存在，继续后续操作')
    else:
        print('压缩文件不存在，退出程序')
        exit()
    if os.path.exists(topath):
        print('文件夹存在，继续后续操作')
    else:
        print('文件夹不存在，马上创建')
        os.mkdir(topath)
    zflen = len(zfile)
    file = zipfile.ZipFile(zpath + '\\' + zfile, 'r')
    for f in file.namelist():
        filename = f.encode('cp437').decode('gbk')
        print(filename)
        if filename != '':
            try:
                # content=file.read(f).decode('utf-8')
                content = file.read(f).decode('utf-8')
            except Exception as err:
                logfile.write(str(err) + "\n")
                infofile.write('文件' + filename + "类型错误\n")
                continue
            content = list(content.split('\r\n'))
            where = ''
            dic = {}
            for line in content:
                if line != '':
                    # print('后11位'+line[-11:])
                    if line[-11:].isdigit():
                        where = where + line + ','
                    dic[line] = -2
            where = where[:-1]
            print(where)
            sql = 'select num,code from status where num in(' + where + ')'
            print(sql)
            result1 = select(sql)
            for m, n in result1:
                print('字典' + str(m) + '\t' + str(n))
                dic[str(m)] = n
            print(dic)
            print(result1)
            filenamestr = topath + '\\' + filename
            # print(filenamestr)
            finalfile = open(filenamestr, 'w', encoding='utf-8')
            for k in dic:
                finalfile.write(k + "\t" + str(dic[k]) + "\n")
            finalfile.close()
    logfile.close()
    file.close()
    infofile.close()
# readzip()


def addzip(pathf='E:\\temp', patht='E:\\fileforuser'):
    tofile = patht + '\\' + 'exam.zip'
    newzip = zipfile.ZipFile(tofile, 'w', zipfile.ZIP_DEFLATED)
    for f in os.listdir(pathf):
        print(f)
        newzip.write(pathf + '\\' + f)
    newzip.close()
addzip()
