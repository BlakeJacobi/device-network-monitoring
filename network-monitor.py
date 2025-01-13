from scapy.all import sniff, ARP, Ether, srp, get_if_list , get_if_addr, get_if_hwaddr
import psutil
import time
import threading

# Function to handle captured packets
def packet_callback(packet):
    print(packet.summary())

# Function to capture packets
def packet_callback(packet):
    print(packet.summary())

def capture_packets():
    print("Available interfaces:")
    interfaces = get_if_list()
    for idx, iface in enumerate(interfaces):
        try:
            ip = get_if_addr(iface)
            mac = get_if_hwaddr(iface)
            print(f"{idx}: {iface} (IP: {ip}, MAC: {mac})")
        except Exception as e:
            print(f"{idx}: {iface} (Error: {e})")
    
    try:
        choice = int(input("Enter the number of the interface to sniff on: "))
        if choice < 0 or choice >= len(interfaces):
            print("Invalid choice. Exiting.")
            return
        interface = interfaces[choice]
        print(f"Starting packet capture on {interface}. Press Ctrl+C to stop...")
        sniff(prn=packet_callback, iface=interface, count=0)
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
    except PermissionError:
        print("Error: Run this script with administrator/root privileges.")

# Function to scan the network
def scan_network(ip_range):
    print(f"Scanning the network range: {ip_range}")
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    answered, _ = srp(request, timeout=2, verbose=False)
    for _, response in answered:
        print(f"IP: {response.psrc}, MAC: {response.hwsrc}")

# Function to monitor bandwidth usage
def monitor_bandwidth():
    print("Monitoring bandwidth usage... Press Ctrl+C to stop.")
    try:
        while True:
            counters = psutil.net_io_counters()
            print(f"Bytes Sent: {counters.bytes_sent}, Bytes Received: {counters.bytes_recv}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped bandwidth monitoring.")

# Main menu
def main():
    while True:
        print("\nNetwork Monitoring Tool")
        print("1. Capture Packets")
        print("2. Monitor Bandwidth")
        print("3. Scan Network")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            capture_packets()
        elif choice == "2":
            monitor_bandwidth()
        elif choice == "3":
            ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
            scan_network(ip_range)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
