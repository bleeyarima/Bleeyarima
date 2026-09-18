#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """Attempt a TCP connection to target:port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target_ip_or_hostname>")
        sys.exit(1)

    target = sys.argv[1]
    # Resolve hostname to IP if needed
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Cannot resolve hostname.")
        sys.exit(1)

    print(f"Scanning target: {target_ip}")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Common ports: 21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445,
                    993, 995, 1723, 3306, 3389, 5900, 8080]

    open_ports = []
    for port in common_ports:
        if scan_port(target_ip, port):
            print(f"Port {port} is open")
            open_ports.append(port)

    if not open_ports:
        print("No common open ports found.")

    print(f"\nScan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()