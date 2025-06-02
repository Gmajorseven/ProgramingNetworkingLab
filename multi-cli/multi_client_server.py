import socket
import threading

def hdl_cli(conn, cli_addr):
    print(f"Connection from {cli_addr}")
    try:
        while True:
            data = conn.recv(1024)
            if data:
                print(f"Received from {cli_addr}: {data.decode('utf-8')}")
                conn.sendall(b"Massage received")
            else:
                break
    finally:
        conn.close()

def start_serv():
    serv_addr = '127.0.0.1'
    serv_port = 65432

    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv_socket.bind((serv_addr, serv_port))

    serv_socket.listen(5)
    print(f"Server is listening on {serv_addr}:{serv_port}")

    while True:
        conn, cli_addr = serv_socket.accept()

        cli_thread = threading.Thread(target=hdl_cli, args=(conn, cli_addr))
        cli_thread.start()

start_serv()