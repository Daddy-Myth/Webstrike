import socket

def scan_ports(host, ports=[21, 22, 80, 443, 3306, 8080]):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((host, port))
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports
