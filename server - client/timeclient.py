import socket

server_ip = input('Enter server IP address: ')
    
client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
client_s.connect((server_ip, 1303))
    
data = client_s.recv(1024)
    
print('Received:', data.decode())
    
client_s.close()