import socket
import struct
import time

def multicast_msg():
    multicast_group = '224.1.1.1'
    multicast_port = 64000

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ttl = struct.pack('b', 1)
    udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    while True:
        msg = "Hello, Multicast!"
        udp_socket.sendto(msg.encode('utf-8'), (multicast_group, multicast_port))
        print(f"Multicasted: {msg}")
        time.sleep(2)

multicast_msg()