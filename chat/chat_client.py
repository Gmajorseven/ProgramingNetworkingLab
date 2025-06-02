import socket
import threading

def recv_msg(cli_socket):
    while True:
        try:
            msg = cli_socket.recv(1024).decode('utf-8')
            if msg:
                print(msg)
        except:
            print("An error occurred!")
            cli_socket.close()
            break

def start_cli():
    serv_addr = '127.0.0.1'
    serv_port = 65432

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cli_socket.connect((serv_addr, serv_port))

    recv_thread = threading.Thread(target=recv_msg, args=(cli_socket,))
    recv_thread.start()

    while True:
        msg = input()
        cli_socket.send(msg.encode('utf-8'))

start_cli()
    