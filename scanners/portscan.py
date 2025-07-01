import socket

def scan_ports(host, ports=[21, 22, 80, 443, 3306, 8080]):
    open_ports = []
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((host, port))
            open_ports.append(port)
            s.close()
        except:
            pass
    return open_ports
