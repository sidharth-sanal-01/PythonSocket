import socket

HOST="127.0.0.1" #loop back IP
PORT=5100

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,recv=s.accept()

    with conn:
        while True:
            data=conn.recv(1024)

            if not data:
                break

            conn.sendall(data)
            print("Data recieved at server:",data)

    