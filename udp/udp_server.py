import socket

def start_serv():
	serv_addr = '127.0.0.1'
	serv_port = 60000

	serv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	serv_sock.bind((serv_addr, serv_port))

	# UDP not able open listen method
	print(f"Server is listening on {serv_addr}:{serv_port}")

	while True:
		data, cli_addr = serv_sock.recvfrom(1024)
		print(f"Received: {data.decode('utf-8')} from {cli_addr}")

		res = b"Message received"
		serv_sock.sendto(res, cli_addr)

start_serv()
