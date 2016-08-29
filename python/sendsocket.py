import socket


def send(data, host='192.168.168.130', port=8001):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        sock.send(str(data).encode('utf-8'))
        receive = sock.recv(10240)
        sock.close()
        result = receive.decode("utf-8")
    except Exception as err:
        result = str(err)
    finally:
        return result
if __name__=="__main__":
	print(send(data={'name': '陈鹏欢', }, host='192.168.168.130'))
