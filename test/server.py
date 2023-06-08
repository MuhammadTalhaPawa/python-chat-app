import socket
import threading

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind(("localhost", 8000))

# Listen for incoming connections
s.listen(2)

print("Server listening on port 8000...")

# Accept a connection 1
client_socket1, client_address1 = s.accept()
print("Connected to client 1:", client_address1)

# Accept a connection 1
client_socket2, client_address2 = s.accept()
print("Connected to client 2:", client_address2)


def rec_msg(client,address):
    data = client.recv(1024).decode()
    print(f'{address}: send: {data}')

    if data == "":
        return False
    else:
        return True
     
run_loop = True

while run_loop:
    thread1 = threading.Thread(target=lambda: setattr(thread1, 'result', rec_msg(client_socket1, client_address1)))
    thread2 = threading.Thread(target=lambda: setattr(thread2, 'result', rec_msg(client_socket2, client_address2)))
    # thread2 = threading.Thread(target=rec_msg,args=(client_socket2,client_address2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    result1 = thread1.result
    result2 = thread2.result

    if result1 == True and result2 == True:
        run_loop = True
    else:     
        run_loop = False
    # run_loop = rec_msg(client_socket1,client_address1)
    

client_socket1.close()
client_socket2.close()
# Close the connection
s.close()
