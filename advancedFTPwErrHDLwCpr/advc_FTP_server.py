import socket
import zlib
import hashlib

def handle_client(client_socket):
    try:
        # Receive the file size
        file_size = int(client_socket.recv(1024).decode('utf-8'))
        client_socket.send("ACK".encode('utf-8'))
        
        # Receive the file data
        received_data = b""
        while len(received_data) < file_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            received_data += packet
        
        # Decompress the received data
        decompressed_data = zlib.decompress(received_data)
        
        # Calculate the received file hash
        received_file_hash = client_socket.recv(64).decode('utf-8')
        
        # Calculate the hash of the received file data
        calculated_hash = hashlib.sha256(decompressed_data).hexdigest()
        
        # Verify the file integrity
        if received_file_hash == calculated_hash:
            with open("received_file", "wb") as file:
                file.write(decompressed_data)
            client_socket.send("File received successfully and verified".encode('utf-8'))
        else:
            client_socket.send("File integrity check failed".encode('utf-8'))
    
    except Exception as e:
        print(f"Error: {e}")
        client_socket.send("Error during file transfer".encode('utf-8'))
    
    finally:
        client_socket.close()

def start_server():
    server_address = '127.0.0.1'
    server_port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)
    print(f"Server is listening on {server_address}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
