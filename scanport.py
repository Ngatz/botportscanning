import socket

def scanport():
    isi = []
    anomalyport = [PORT]
    ip = ("YOUR_IP")
    for port in anomalyport:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0 :
                isi.append(port)
                sock.close()
        
        except socket.error:
            print (f"Could not connect to port {port}")
            return isi
    return isi





