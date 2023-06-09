from connection import Connection 
from file_handler import File_Handler

fh = File_Handler("data.txt")
fh.create_new_file()

index = 0

def append_in_file(ind,sender,mesg):
    data = {
        'index': ind,
        'sender': sender,
        'message': mesg
    }
    fh.append_json_data(data)
    

myServer = Connection()
myServer.init_as_server()
myServer.accept_client_connection()

while True:
    send_mesg = input("Enter message: ")
    if send_mesg == 'exit':
        myServer.end()
        break
    
    append_in_file(index,'server',send_mesg)
    index += 1

    myServer.send_mesg(send_mesg)
    recv_mesg = myServer.recv_mesg()

    if recv_mesg == "":
        myServer.end()
        break
    
    append_in_file(index,'client',recv_mesg)
    index += 1

    print(f'Recieved message: {recv_mesg}')
