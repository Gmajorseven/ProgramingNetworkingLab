import socket
import sys

def scan_ports(host, start_port, end_port):
    
    # Scans a range of ports on a given host to see if they are open.
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    try:
        # Resolve the hostname to an IP address
        target_ip = socket.gethostbyname(host)
        print(f"Resolved {host} to {target_ip}")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            sock.settimeout(1)
            # Try to connect
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            sock.close()

    except socket.gaierror:
        print(f"Error: Hostname could not be resolved: {host}")
        sys.exit()
    except socket.error:
        print(f"Error: Could not connect to server.")
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting scan.")
        sys.exit()

    return open_ports

if __name__ == "__main__":
    try:
        target_host = input("Enter the host to scan: ")
        start = int(input("Enter the start port: "))
        end = int(input("Enter the end port: "))

        if start > end or start < 1:
            print("Invalid port range. Please try again.")
        else:
            found_ports = scan_ports(target_host, start, end)
            if found_ports:
                print(f"Scan complete. Open ports: {found_ports}")
            else:
                print("Scan complete. No open ports found in the specified range.")

    except ValueError:
        print("Invalid input. Please enter a valid number for ports.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
