import socket
import sys


def get_this_pc_information():
    hostname = socket.gethostname()
    ip = socket.gethostbyname_ex(hostname)[-1][-1]
    print("HOSTNAME:  %s" % hostname)
    print("IP:  %s" % ip)
    return ( hostname, ip)


# Create a TCP/IP socket    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
(hostname,server_address) = get_this_pc_information()
# Bind the socket to the port
sock.bind(('0.0.0.0', 10000))

while True:
    print ( server_address , '\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print (server_address, 'received %s bytes from %s' % (len(data), address))
    print (server_address, data)

    if data:
        sent = sock.sendto(data, address)
        print(server_address, 'sent %s bytes back to %s' % (sent, address))
        break

sock.close()