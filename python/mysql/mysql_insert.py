import pymysql
import time
start = time.time()
conn = pymysql.connect(host='192.168.1.183', port=3306,user='cph', passwd='123123',db='cph', charset='UTF8')
cur = conn.cursor()
for i in range(0, 1000):
    cur.execute("INSERT INTO `cph` VALUES("+str(i)+")")
conn.commit()
cur.close()
conn.close()
stop = time.time()
print(stop-start)
