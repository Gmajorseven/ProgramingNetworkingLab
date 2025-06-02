import ipaddress

def calculate_network_details(ip_address_str, cidr_prefix):
    """
    Calculates and prints network details for a given IPv4 address and CIDR prefix.

    Args:
        ip_address_str (str): The IP address in dot-decimal notation (e.g., "192.168.1.10").
        cidr_prefix (int): The CIDR prefix length (e.g., 24 for /24).
    """
    try:
        # Combine IP address and CIDR prefix into a network object
        # This automatically calculates the network address and broadcast address
        network_str = f"{ip_address_str}/{cidr_prefix}"
        ip_network = ipaddress.ip_network(network_str, strict=False)
        # strict=False allows the input IP to be a host address within the network,
        # not necessarily the network address itself.

        print(f"--- Network Details for {ip_address_str}/{cidr_prefix} ---")
        print(f"IP Address Provided: {ip_address_str}")
        print(f"CIDR Prefix Length: /{cidr_prefix}")
        print(f"Subnet Mask: {ip_network.netmask}")
        print(f"Network Address: {ip_network.network_address}")
        print(f"Broadcast Address: {ip_network.broadcast_address}")

        # Calculate usable host range
        # ip_network.hosts() returns an iterator of usable host addresses
        usable_hosts = list(ip_network.hosts())

        if usable_hosts:
            first_usable_ip = usable_hosts[0]
            last_usable_ip = usable_hosts[-1]
            num_usable_hosts = len(usable_hosts)
            print(f"First Usable Host IP: {first_usable_ip}")
            print(f"Last Usable Host IP: {last_usable_ip}")
            print(f"Number of Usable Hosts: {num_usable_hosts}")
        else:
            # This case handles /31 (point-to-point) and /32 (single host) networks
            # where there are no "usable" hosts in the traditional sense.
            print("No usable host addresses in this network (e.g., /31 or /32).")

    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure the IP address is valid and the CIDR prefix is between 0 and 32 for IPv4.")

# --- User Input ---
if __name__ == "__main__":
    while True:
        ip_input = input("Enter the IPv4 address (e.g., 192.168.1.10): ")
        cidr_input = input("Enter the CIDR prefix length (e.g., 24): ")

        try:
            cidr_prefix_int = int(cidr_input)
            calculate_network_details(ip_input, cidr_prefix_int)
            break # Exit loop after successful calculation
        except ValueError:
            print("Invalid CIDR prefix. Please enter an integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        print("\n" + "="*50 + "\n") # Separator for next attempt
