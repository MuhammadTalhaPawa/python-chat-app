import socket

def run_client():
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode())

        if message.lower() == "exit chat":
            break

    client_socket.close()

run_client()
