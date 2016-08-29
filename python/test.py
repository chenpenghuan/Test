#!/usr/bin/env python3
# encoding: utf-8
from pymysql import connect
conf={}
def readconf():
    try:
        conn = connect(host='127.0.0.1', user='root',passwd='123123',db='winnerlook',port=3306,charset='utf8')
        cur = conn.cursor()
        sql = 'select item_id,id,cont_var,cont_url,cont_sec,cont_title from cont_conf'
        cur.execute(sql)
        data=cur.fetchall()
    except Exception as err:
        data='connection error: '+str(err)
    finally:
        return data
data=readconf()
for i in data:
    #if i[1] is not None:
    if conf.get(i[0]) is None:
        conf[i[0]]={}
    conf[i[0]][i[1]]={"cont_var":i[2],"cont_url":i[3]}
print(conf)


