from connection import Connection

myClient = Connection()
myClient.init_as_client()

while True:
    recv_mesg = myClient.recv_mesg()
    print(f'Recieved message: {recv_mesg}')
    
    send_mesg = input("Enter message: ")
    if send_mesg == 'exit':
        myClient.end()
        break
    myClient.send_mesg(send_mesg)

# myServer.init_as_server()
# myServer.accept_client_connection()


