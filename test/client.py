import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(("localhost", 8000))
print("Connected to server")


while True:
    # Send a message to the server
    message = input("Enter Message: ")
    s.send(message.encode())

# Close the connection
s.close()
