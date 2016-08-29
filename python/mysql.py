def select(sql):
    import pymysql
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123123',
            db='mysite',
            port=3306,
            charset='utf8')
        cur = conn.cursor()  # 获取mysql'
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
    except Exception as err:
        result = str(err)
    finally:
        return result
print(select('select * from users')[0])
'''
import hashlib
m = hashlib.md5()
m.update('cph'.encode('utf-8'))
print(m.hexdigest())
'''
