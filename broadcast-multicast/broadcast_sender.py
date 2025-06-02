import socket
import time

def broadcast_msg():
    broadcast_addr = '127.0.0.1'
    broadcast_port = 65000

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        msg = "Hello, Broadcast!"
        udp_socket.sendto(msg.encode('utf-8'), (broadcast_addr, broadcast_port))
        print(f"Broadcasted: {msg}")
        time.sleep(2)

broadcast_msg()
