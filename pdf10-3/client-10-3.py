import socket
import time
name=["zeynab","zahra","fatemeh","kosar","zeynabb"]
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1',60000))
    for i in name:
        s.sendall(i.encode())
        data=s.recv(1024)
        data.decode()
        print(data)
        time.sleep(3)

