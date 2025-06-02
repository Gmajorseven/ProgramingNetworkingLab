import socket

def start_cli():
	serv_addr = '127.0.0.1'
	serv_port = 65432

	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	cli_sock.connect((serv_addr, serv_port))

	try:
		massage = "Hello, Server!"
		cli_sock.sendall(massage.encode('utf-8'))
		res = cli_sock.recv(1024)
		print(f"Received: {res.decode('utf-8')}")
	
	finally:
		cli_sock.close()

start_cli()
