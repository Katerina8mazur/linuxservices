import socket
import datetime

server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_s.bind(('0.0.0.0', 1303))

server_s.listen(1)
    
print('Server started')
    
while True:
    client_s, client_addr = server_s.accept()
        
    print('Client connected:', client_addr)
        
    current_time = datetime.datetime.now()
    time_str = current_time.strftime('%d.%m.%Y %H:%M')
        
    client_s.send(time_str.encode())
        
    client_s.close()
        
    print('Connection closed')
