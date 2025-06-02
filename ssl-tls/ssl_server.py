import socket
import ssl


def start_server():
    server_addr = '127.0.0.1'
    server_port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((server_addr, server_port))

    server_socket.listen(5)
    print(f"Server is listening on {server_addr}:{server_port}")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile='./certificate.pem', keyfile='./priv_key.pem')

    while True:
        cli_socket, cli_addr = server_socket.accept()
        print(f"Connection from {cli_addr}")

        ssl_cli_socket = context.wrap_socket(cli_socket, server_side=True)

        try:
            msg = ssl_cli_socket.recv(1024).decode('utf-8')
            print(f"Received from {cli_addr}: {msg}")
            ssl_cli_socket.send("Message received securely".encode('utf-8'))
        finally:
            ssl_cli_socket.close()


start_server()

