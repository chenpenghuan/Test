def scan_mysql():
    global conn
    conn = ''
connect(host='localhost', user='root', passwd='123123',
        db='test', port=3306, charset='utf8')
    global cur
    cur = conn.cursor()
    findtask(3)
    cur.close()
    conn.close()


def findtask(waittime):
    sleep(waittime)
    cur.execute(
        'select taskid,username,tasktime,taskcode,upload,download,tasklevel,taskstatus from taskinfo where taskstatus=0 order by tasklevel limit 1')
    data = cur.fetchall()
    if(len(data) > 0):
        print('发现任务，信息如下，交给大数据平台处理')
        print(data)
        flag = input('大数据平台处理结束，返回信号')
        if flag:
            print('大数据处理完了，查找下一个任务')
            findtask(waittime)
scan_mysql()
