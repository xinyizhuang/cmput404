import socket
import socketserver


#HOST, PORT = '', 8888

#listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#listen_socket.bind((HOST, PORT))
#listen_socket.listen(1)

#print("serving HTTP on port %s ..." % PORT)
class MyWebServer(socketserver.BaseRequestHandler):
    def handler(self):
        
        while True:
            #client_connection, client_address = listen_socket.accept()
            
            self.conn, self.addr = self.request
            request = client_connection.recv(1024)
            print(request)
            
            http_response = """\
            HTTP/1.1 200 OK
            
            Hello, World!
            """
            
            client_connection.sendall(http_response.encode())
            client_connection.close()
        
if __name__ == "__main__":
    
    HOST, PORT = "localhost", 8080
    
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)
    
    server.serve_forever()