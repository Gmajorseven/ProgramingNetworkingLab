import socket

def handle_request(request):
    # Parse HTTP request
    headers = request.split('\r\n')
    first_line = headers[0].split(' ')
    method = first_line[0]
    path = first_line[1]

    # Generate response based on request method
    if method == 'GET':
        return handle_get(path)
    elif method == 'POST':
        return handle_post(headers, request)
    else:
        return 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'

def handle_get(path):
    if path == '/':
        path = '/index.html'
    
    try:
        with open(f'.{path}', 'r') as file:
            content = file.read()
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'

    return response

def handle_post(headers, request):
    # For simplicity, we won't actually handle POST data in this example
    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nPOST request received'
    return response

def start_server():
    server_address = '127.0.0.1'
    server_port = 8080

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((server_address, server_port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {server_address}:{server_port}")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the request
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Request: {request}")

        # Handle the request and generate a response
        response = handle_request(request)

        # Send the response
        client_socket.sendall(response.encode('utf-8'))

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
