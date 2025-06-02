import socket

def start_server():
    # Define server address and port
    server_address = '127.0.0.1'
    server_port = 65432

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((server_address, server_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {server_address}:{server_port}")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")

            # Receive the data in small chunks and print it
            while True:
                data = connection.recv(1024)
                if data:
                    print(f"Received: {data.decode('utf-8')}")
                    # Send a response back to the client
                    connection.sendall(b"Message received")
                else:
                    break
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()