import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        # print(f"Received from {client_address}: {message}")
        # Forward the message to the other client
        other_client = clients[1] if client_socket == clients[0] else clients[0]
        other_client.send(message.encode())

    client_socket.close()

def run_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server listening on {}:{}".format(host, port))

    while True:
        # is_client_first_connected = False
        for client in clients:
            print(client)

        a = input("Enter Code:");
        if(a == "exit"):
            break
        client_socket, addr = server_socket.accept()
        print("Connected with", addr)
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

    server_socket.close()


clients = []

run_server()



# import socket
# import threading

# def handle_client(client_socket):
#     while True:
#         message = client_socket.recv(1024).decode()
#         if not message:
#             break
#         print("Received message:", message)
#         response = input("Enter your response: ")
#         client_socket.send(response.encode())

#     client_socket.close()

# def run_server():
#     host = 'localhost'
#     port = 8888

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(5)
#     print("Server listening on {}:{}".format(host, port))

#     while True:
#         # if(len(clien))
#         for client in clients:
#             print(client)
#         client_socket, addr = server_socket.accept()
#         print("Connected with", addr)
#         clients.append(client_socket)
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()


# clients = []

# run_server()



# # import socket
# # import threading

# # def handle_client(client_socket):
# #     while True:
# #         message = client_socket.recv(1024).decode()

# #     # while True:
# #     #     message = client_socket.recv(1024).decode()
# #     #     if not message:
# #     #         break
# #     #     print("Received message:", message)
# #     #     response = input("Enter your response: ")
# #     #     client_socket.send(response.encode())

# #     client_socket.close()

# # def run_server():
# #     host = 'localhost'
# #     port = 8888

# #     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     server_socket.bind((host, port))
# #     server_socket.listen(5)
# #     print("Server listening on {}:{}".format(host, port))

# #     while True:
# #         client_socket, addr = server_socket.accept()
# #         print("Connected with", addr)
# #         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
# #         client_thread.start()

# # run_server()
