import socket
import struct

def recv_multicast():
    multicast_group = '224.1.1.1'
    multicast_port = 64000

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('', multicast_port))

    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f"Listening for multicast message on {multicast_group}:{multicast_port}")

    while True:
        msg, addr = udp_socket.recvfrom(1024)
        print(f"Received from {addr}: {msg.decode('utf-8')}")

recv_multicast()