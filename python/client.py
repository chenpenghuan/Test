import socket
import time
if "__main__" == __name__:
    # sock.send(json.dumps({'username':'陈鹏欢','password':'123123'}).encode('utf-8'))
    for item in range(0, 10):
        time.sleep(3)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.1.198', 8001))
        sock.send(str(item).encode('utf-8'))
        szBuf = sock.recv(1024)
        byt = 'recv:' + szBuf.decode('utf-8')
        print(byt)
        sock.close()
