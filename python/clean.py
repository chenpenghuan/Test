from sys import argv,exit
try:
    filef=argv[1]
except IndexError:
    print('程序错误:请指定输入文件')
    exit()
try:
    filet=argv[2]
except IndexError:
    print('程序错误:请指定输出文件')
    exit()
dic={}
with open(filef,encoding='utf-8',newline='') as f1:
    for l in f1:
        l=l.split()
        if len(l)>0:
            if l[0] in dic.keys():
                dic[l[0]]=dic[l[0]]+1
            else:
                dic[l[0]]=1
with open(filet,'w',encoding='utf-8',newline='') as f2:
    for i in dic:
        f2.write(i+"\r\n")
