import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Received from server:", message)

    client_socket.close()

def run_client():
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

        if message.lower() == "exit":
            break

    client_socket.close()

run_client()


# import socket

# def run_client():
#     host = 'localhost'
#     port = 8888

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))

#     print('in run client')


# run_client()

# # import socket

# # def run_client():
# #     host = 'localhost'
# #     port = 8888

# #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     client_socket.connect((host, port))

# #     while True:
# #         message = input("Enter message: ")
# #         client_socket.send(message.encode())
# #         response = client_socket.recv(1024).decode()
# #         print("Server response:", response)

# #         if message.lower() == "exit":
# #             break

# #     client_socket.close()

# # run_client()
