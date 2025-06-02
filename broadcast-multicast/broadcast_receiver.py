import socket

def recv_broadcast():
    listen_addr = '0.0.0.0'
    listen_port = 65000

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind((listen_addr, listen_port))

    print(f"Listening for broadcasts on {listen_addr}:{listen_port}")

    while True:
        msg, addr = udp_socket.recvfrom(1024)
        print(f"Received from {addr}: {msg.decode('utf-8')}")

recv_broadcast()