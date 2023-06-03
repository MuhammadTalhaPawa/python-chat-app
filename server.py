import socket
import threading

debug_exit = False

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if message == 'exit server':
            debug_exit = True
        if not message:
            break
        print(f"Received from {client_address}: {message}")
        # Forward the message to the other client
        # other_client = clients[1] if client_socket == clients[0] else clients[0]
        # other_client.send(message.encode())

    client_socket.close()

def run_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server listening on {}:{}".format(host, port))

    while True:
        if debug_exit:
            break
        client_socket, addr = server_socket.accept()
        print("Connected with", addr)
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

    server_socket.close()


clients = []

run_server()


