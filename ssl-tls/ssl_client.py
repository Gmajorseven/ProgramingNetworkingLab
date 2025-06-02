import socket
import ssl


def start_client():
    server_addr = '127.0.0.1'
    server_port = 65432

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('./certificate.pem')
    context = ssl._create_unverified_context()

    ssl_cli_socket = context.wrap_socket(
        cli_socket, server_hostname=server_addr
    )

    ssl_cli_socket.connect((server_addr, server_port))

    try:
        msg = "Hello, Secure Server!"
        ssl_cli_socket.send(msg.encode('utf-8'))
        res = ssl_cli_socket.recv(1024).decode('utf-8')
        print(f"Received: {res}")
    finally:
        ssl_cli_socket.close()


start_client()
