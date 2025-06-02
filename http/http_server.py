import socket
def handle_req(req):
    headers = req.split('\r\n')
    first_line = headers[0].split(' ')
    method = first_line[0]
    path = first_line[1]

    if method == 'GET':
        return handle_get(path)
    elif method == 'POST':
        return handle_post(headers, req)
    else:
        return 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'

def handle_get(path):
    if path == '/':
        path = '/index.html'
    try:
        with open(f'.{path}', 'r') as file:
            content = file.read()
        res = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
    except FileNotFoundError:
        res = 'HTTP/1.1 404 Not Found\r\n\r\n'
    return res

def handle_post(headers, req):
    res = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nPOST request received'
    return res

def start_server():
    server_addr = '127.0.0.1'
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_addr, server_port))
    server_socket.listen(5)
    print(f"Server is listening on {server_addr}:{server_port}")
    while True:
        cli_socket, cli_addr = server_socket.accept()
        print(f"Connection from {cli_addr}")
        req = cli_socket.recv(1024).decode('utf-8')
        print(f"Request: {req}")
        res = handle_req(req)
        cli_socket.sendall(res.encode('utf-8'))
        cli_socket.close()
if __name__ == "__main__":
    start_server()

