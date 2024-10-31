
import threading
import socket



def handleSocket(client_socket,client_add):
    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        
        print(f"Recieved data from add{client_add}:{data.decode('utf-8')}")
        client_socket.sendall(data)
    client_socket.close()
    print(f"closed connection on {client_add}")


def main():
    host="127.0.0.1"
    port=5202

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:

        server_socket.bind((host,port))

        server_socket.listen(5)

        print("Server is listening on port 5200")
        no_of_active_connections=0
        while True:
            
            client_socket,client_addr=server_socket.accept()
            no_of_active_connections+=1
            
            client_thread=threading.Thread(target=handleSocket,args=(client_socket,client_addr))
            print("Number of active connections: ",no_of_active_connections)
            client_thread.start()
        
        
        
if __name__=="__main__":
    main()