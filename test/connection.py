import socket

class Connection:    
    #  initializeing as server
    def init_as_server(self):
        self.connected_as = "server"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8000))
        self.server_socket.listen(1)

    # initializing as client
    def init_as_client(self):
        self.connected_as = "client"
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8000))
        print("Connected to server.")

    # Connect the server to the one client
    def accept_client_connection(self):
        print("Server started, waiting for connections...")
        self.client_socket, self.address = self.server_socket.accept()
        print("Connected to", self.address)

    def recv_mesg(self):
        message = self.client_socket.recv(1024).decode()
        return message

    def send_mesg(self,mesg):
        self.client_socket.send(mesg.encode())

    def end(self):
        if self.connected_as == "server":
            self.server_socket.close()

        self.client_socket.close()
        
