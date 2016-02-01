import socket
import StringIO
import sys
from email.mime import application

class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1
    
    def __init__(self,server_address):
        
        self.listen_socket = listen_socket = socket.socket(self.address_family,self.socket_type)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        
        listen_socket.listen(self.request_queue_size)
        
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name= socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []
        
    def set_app(self, application):
        self.application = application
        
    def server_forver(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection,client_address = listen_socket.accept()
            self.handle_one_request()
            
    def handle_one_request(self):
             self.request_data = request_data = self.client_connection.recv(1024)
               print(''.join(
            '&lt; {line}n'.format(line=line)
            for line in request_data.splitlines()))
             
    
    
    
    
    
    
    
    
    
    
    
    
    