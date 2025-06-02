import socket

def start_client():
	serv_addr = '100.121.1140.122'
	serv_port = 65432

	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	cli_sock.connect((serv_addr, serv_port))

	file_path = 'requirements.txt'
	with open(file_path, 'rb') as file:
		while True:
			data = file.read(1024)
			if not data:
				break
			cli_sock.sendall(data)

		cli_sock.close()
		print(f"File '{file_path}' sent to the server completed.")

if __name__ == "__main__":
	start_client()

