import socket
import subprocess
import platform
import re

def network_recon():
    """Perform internal network reconnaissance."""
    print("🔍 Network Reconnaissance")
    print("=" * 50)

    # Internal IP ranges
    print("🌐 Internal IP Address:")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP: {ip}")
        
        # Check common internal ranges
        if re.match(r"^(10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.|192\.168\.)", ip):
            print("→ Belongs to private IP range")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

    # Gateway
    print("🚪 Gateway:")
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
            match = re.search(r"Default Gateway[.\s]*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", result.stdout)
        else:
            result = subprocess.run(["ip", "route"], capture_output=True, text=True)
            match = re.search(r"default via (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", result.stdout)
        if match:
            print(f"Default Gateway: {match.group(1)}")
        else:
            print("Gateway not found")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

    # DNS servers
    print("📡 DNS Servers:")
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
            dns_list = re.findall(r"DNS Servers[.\s]*: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", result.stdout)
        else:
            with open("/etc/resolv.conf", "r") as f:
                content = f.read()
            dns_list = re.findall(r"nameserver (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", content)
        for dns in dns_list:
            print(f"DNS Server: {dns}")
        if not dns_list:
            print("No DNS servers found")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

    # Open local services (scan common ports)
    print("🔌 Open Local Services (on localhost):")
    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
        443: "HTTPS", 3389: "RDP", 3306: "MySQL", 5432: "PostgreSQL"
    }
    open_ports = []
    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            open_ports.append(f"{port}/{service}")
        sock.close()
    if open_ports:
        print("Open ports:", ", ".join(open_ports))
    else:
        print("No common open ports found")
    print("=" * 50)

# Run the function
network_recon()   