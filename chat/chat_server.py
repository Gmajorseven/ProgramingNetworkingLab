import socket
import threading

clients = []

def broadcast(msg, current_cli):
    for cli in clients:
        if cli != current_cli:
            try:
                cli.send(msg)
            except:
                cli.close()
                clients.remove(cli)

def hdl_cli(cli_socket):
    while True:
        try:
            msg = cli_socket.recv(1024)
            if msg:
                broadcast(msg, cli_socket)
            else:
                break
        except:
            clients.remove(cli_socket)
            cli_socket.close()
            break

def start_serv():
    serv_addr = ''
    serv_port = 65432

    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind((serv_addr, serv_port))

    serv_socket.listen(5)
    print(f"Server is listening from {serv_addr}:{serv_port}")

    while True:
        cli_socket, cli_addr = serv_socket.accept()
        print(f"Connection from {cli_addr}")

        clients.append(cli_socket)

        cli_thread = threading.Thread(target=hdl_cli, args=(cli_socket,))
        cli_thread.start()
    

start_serv()