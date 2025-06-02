import socket
import select

def start_sever():
    server_addr = '127.0.0.1'
    server_port = 65432

    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setblocking(False)

    serv_sock.bind((server_addr, server_port))

    serv_sock.listen(5)
    print(f"Server is listening on {server_addr}:{server_port}")

    sockets_list = [serv_sock]
    clients = {}

    def recv_msg(cli_sock):
        try:
            msg = cli_sock.recv(1024)
            if not msg:
                return False
            return msg.decode('utf-8')
        except:
            return False
    
    while True:
        read_sock, _, exception_sock = select.select(sockets_list, [], sockets_list)

        for notified_sock in read_sock:
            if not notified_sock == serv_sock:
                cli_sock, cli_addr = serv_sock.accept()
                cli_sock.setblocking(False)
                sockets_list.append(cli_sock)
                clients[cli_sock] = cli_addr
                print(f"Accepted new connection from {clients[notified_sock]}")
            else:
                msg = recv_msg(notified_sock)
                if msg is False:
                    print(f"Closed connection from {clients[notified_sock]}")
                    sockets_list.remove(notified_sock)
                    del clients[notified_sock]
                    continue
                print(f"Received mesafe from {clients[notified_sock]}: {msg}")
                notified_sock.send("Message received".encode('utf-8'))
        
        for notified_sock in exception_sock:
            sockets_list.remove(notified_sock)
            del clients[notified_sock]

start_sever()