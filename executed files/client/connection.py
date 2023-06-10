import socket
import json

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

    def recv_json_array(self):
        receive_buffer = bytearray(1024)
        received_data = bytearray()

        while True:
            # Receive data into the buffer
            received_bytes = self.client_socket.recv_into(receive_buffer)
            
            # Check if the received data exceeds the buffer size
            if received_bytes > len(receive_buffer):
                # Dynamically adjust the buffer size to accommodate the received data
                receive_buffer.extend(bytearray(received_bytes - len(receive_buffer)))
            
            # Append the received data to the overall received_data
            received_data += receive_buffer[:received_bytes]
            
            # Check if all data has been received
            if received_bytes < len(receive_buffer):
                break

        data = received_data.decode('utf-8')


        # data = self.client_socket.recv(1024).decode('utf-8')
        # Convert the received JSON string back to an array
        json_array = json.loads(data)
        return json_array

    def send_mesg(self,mesg):
        self.client_socket.send(mesg.encode())

    def send_json_array(self,json_array):
        json_string = json.dumps(json_array)
        self.client_socket.sendall(json_string.encode('utf-8'))

    def end(self):
        if self.connected_as == "server":
            self.server_socket.close()

        self.client_socket.close()
        
