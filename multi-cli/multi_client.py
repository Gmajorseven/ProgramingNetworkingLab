import socket

def start_cli(msg):
    serv_addr = '127.0.0.1'
    serv_port = 65432

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cli_socket.connect((serv_addr, serv_port))

    try:
        cli_socket.sendall(msg.encode('utf-8'))

        res = cli_socket.recv(1024)
        print(f"Received: {res.decode('utf-8')}")
    finally:
        cli_socket.close()

msg = "Hello from client!"
start_cli(msg)