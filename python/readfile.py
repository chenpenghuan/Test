#号码清洗使用
import sys
dic = {}
filef=sys.argv[1]
filet1=sys.argv[2]
filet2=sys.argv[3]
status=sys.argv[4]
with open(filef, 'r') as f:
    for line in f:
        line=line.split()
        if len(line):
            dic[line[0]] = -2
with open(filet1, 'w') as rf1:
        with open(status, 'r') as f:
            for line in f:
                line = line.split()
                if dic.get(line[0]):
                    rf1.write(line[0] + "\t" + line[1] + "\r\n")
                    dic.pop(line[0])
with open(filet2, 'w') as rf2:
    for i in dic:
        rf2.write(str(i) + "\r\n")

