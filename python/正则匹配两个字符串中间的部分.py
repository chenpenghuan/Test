import re
#文本所在TXT文件
file = 'content.txt'
#关键字1,2(修改引号间的内容)
w1 = '【'
w2 = '】'
f = open(file,'r')
buff = f.read()
f.close()
#清除换行符,请取消下一行注释
#buff = buff.replace('\n','')
pat = re.compile(w1+'(.*?)'+w2,re.S)
result = pat.findall(buff)
print(result)
sad