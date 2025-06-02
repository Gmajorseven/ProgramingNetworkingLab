import socket
import zlib
import hashlib

def send_file(file_path, server_address, server_port):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Compress the file data
        compressed_data = zlib.compress(file_data)
        
        # Calculate the file hash
        file_hash = hashlib.sha256(file_data).hexdigest()
        
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        client_socket.connect((server_address, server_port))
        
        # Send the file size
        client_socket.send(str(len(compressed_data)).encode('utf-8'))
        client_socket.recv(3)  # Wait for ACK
        
        # Send the compressed file data
        client_socket.sendall(compressed_data)
        
        # Send the file hash
        client_socket.send(file_hash.encode('utf-8'))
        
        # Receive the server response
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    file_path = "file_to_send"
    server_address = '127.0.0.1'
    server_port = 65432
    send_file(file_path, server_address, server_port)
