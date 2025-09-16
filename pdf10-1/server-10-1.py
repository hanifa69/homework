import socket 
import datetime
HOST= '127.0.0.1'
PORT=60000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("Server is listening on 127.0.0.1 , 60000")
    conn,addr= s.accept()
    print(f"Connected by {addr}")
    with conn:
        while True:
            a= conn.recv(1024)
            a=a.decode()
            if a=="d":
                data=datetime.datetime.today().strftime("%Y-%m-%d")
            elif a=="t":
                data=datetime.datetime.now().strftime("%H:%M:%S")
            

            conn.sendall(data.encode())

     