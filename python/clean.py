from os import path
from json import loads
# from config import fileold, filenew, result
if path.isfile('config.json'):
	pass
else:
	print('找不到config.json文件，请检查')
	exit()
conf = open('config.json', 'r')
confstr = conf.read()
conf.close()
fileold = loads(confstr)['fileold']
filenew = loads(confstr)['filenew']
result = loads(confstr)['result']
for i in fileold:
    if path.isfile(i):
        pass
    else:
        print('历史文件' + i + '不存在，请检查配置文件config.py')
        exit()
for i in filenew:
    if path.isfile(i):
        pass
    else:
        print('比对文件' + i + '不存在，请检查配置文件config.py')
        exit()
dic = {}
for fo in fileold:
    with open(fo, encoding='utf-8', newline='') as f1:
        for l in f1:
            l = l.split()
            if len(l) > 0:
                if l[0] in dic.keys():
                    dic[l[0]] = dic[l[0]] + 1
                else:
                    dic[l[0]] = 1
dic2 = {}
if len(dic) > 0:
    for fn in filenew:
        with open(fn, encoding='utf-8', newline='') as f2:
            for i in f2:
                i = i.split()
                if len(i):
                    if len(i[0]) == 11 and i[0].isdigit() and i[
                            0] not in dic.keys():
                        dic2[i[0]] = 1
else:
    for fn in filenew:
        with open(fn, encoding='utf-8', newline='') as f2:
            for i in f2:
                i = i.split()
                if len(i):
                    if len(i[0]) == 11 and i[0].isdigit():
                        dic2[i[0]] = 1
resultfile = open(result[0], 'w', encoding='utf-8', newline='')
for i in dic2:
    resultfile.write(str(i) + "\r\n")
resultfile.close()
