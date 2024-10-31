import socket

HOST="127.0.0.1"
PORT=5203

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((HOST,PORT))
    while True:
        input_data=input("Enter data to send to client: ")
        client.sendall(input_data.encode())
        
        data=client.recv(1024)
        print("Recieved from server:",data)