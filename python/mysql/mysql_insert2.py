import datetime
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = conn.cursor()
conn.select_db('python')
starttime = datetime.datetime.now()
print starttime
for j in range(50000):
    values = []
    for i in range(40):
        values.append((i + j * 40, 'fdf' + str(i + j * 40)))
    cursor.executemany("""insert into test values(%s,%s) """, values)
    conn.commit()
cursor.close()
endtime = datetime.datetime.now()
print endtime
print(endtime - starttime).seconds
