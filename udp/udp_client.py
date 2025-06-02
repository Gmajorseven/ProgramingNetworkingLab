import socket

def start_cli():
	serv_addr = '127.0.0.1'
	serv_port = 60000

	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	message = "Hi!, This is a testing MSG: via UDP" 
	cli_sock.sendto(message.encode('utf-8'), (serv_addr, serv_port))

	res, serv = cli_sock.recvfrom(1024)
	print(f"Receiverd: {res.decode('utf-8')} from {serv}")

	cli_sock.close()

start_cli()

