import socket
def receive(host='127.0.0.1',port=8001):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(10)
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(10)
            buf = connection.recv(10240)
            connection.send(say(buf))
        except socket.timeout:
            print('time out')
        finally:
            connection.close()
def say(data):
    return '我收到了你发送的请求，内容是'.encode('utf-8')+data

receive()
