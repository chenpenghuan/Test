import json
import pymysql
with open('config.json', 'r') as f:
    conf = json.load(f)
conn = pymysql.connect(
    host=conf['hostname'],
    user=conf['username'],
    passwd=conf['password'],
    db=conf['database'],
    port=conf['port'])
if conf['action'] == 'select':
    cur = conn.cursor()
    count = cur.execute(conf['sql'])
    result = cur.fetchall()
    cur.close()
    conn.close()
    print('共有'+str(count)+'条数据,内容如下:'+json.dumps(result))
else:
    if conf['action'] == 'insert':
        cur = conn.cursor()
        cur.execute(conf['sql'])
        cur.close()
        conn.close()
