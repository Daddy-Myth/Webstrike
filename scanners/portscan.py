import socket

def scan_ports(host, ports=[21, 22, 23, 69, 80, 111, 135, 137, 138, 139, 1433, 1900, 3306, 3389, 443, 445, 8080,6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669]):
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
