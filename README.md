Network Monitoring Tool
This script provides three key network monitoring functionalities:

Capture Packets: It allows you to capture and display network packets on a selected interface using Scapy. It lists available network interfaces and their IP/MAC addresses and then allows you to sniff packets on a chosen interface.

Monitor Bandwidth: Using the psutil library, this function monitors the bandwidth usage of the system, displaying the total bytes sent and received over time.

Network Scan: This function uses ARP requests to scan a given IP range and display the IP and MAC addresses of active devices on the network.

Key Learnings:
Scapy: Capturing and analyzing network traffic.
psutil: Monitoring bandwidth usage in real-time.
ARP Scanning: Identifying devices on the local network using ARP requests.
