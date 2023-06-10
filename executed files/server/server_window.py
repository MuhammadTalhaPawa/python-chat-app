import tkinter
from tkinter import ttk
import file_handler
import threading
from connection import Connection 

fh = file_handler.File_Handler("data.txt")
fh.create_new_file()

myServer = Connection()
myServer.init_as_server()
myServer.accept_client_connection()
myServer.send_json_array(fh.read_json_array())


window = tkinter.Tk()
window.title("Server Window")
window.geometry("400x300")

def mesg_entered(a = None):
    msg = enter_message_text.get()
    if msg == "":
        return
    enter_message_text.delete(0, tkinter.END)
    print(f'Entered text: {msg}')

    fh.append_json_data({"index": fh.get_last_json()['index']+1, "sender": "server", "message": msg})
    myServer.send_json_array(fh.read_json_array())
    read_and_update_data()

def meg_recv():
    while True:
        recv_mesg = myServer.recv_mesg()
        if recv_mesg =="":
            return
        if recv_mesg.startswith("DELETE"):
            delete_request_index = recv_mesg.split(':')[1].strip()
            # print(recv_mesg)
            # print(delete_request_index)
            # print(f'Delete requrest: {delete_request_index}')
            fh.del_json_with_index(int(delete_request_index))
            myServer.send_json_array(fh.read_json_array())   
        else:
            fh.append_json_data({"index": fh.get_last_json()['index']+1, "sender": "client", "message": recv_mesg})
            myServer.send_json_array(fh.read_json_array())
        read_and_update_data()

enter_text_label = tkinter.Label(window, text="Enter text:")
enter_text_label.pack()

enter_message_text = tkinter.Entry(window)
enter_message_text.pack()

message_send_button = tkinter.Button(window, text="send", command=mesg_entered)
message_send_button.pack()

scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

canvas = tkinter.Canvas(window, yscrollcommand=scrollbar.set)
canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

scrollbar.config(command=canvas.yview)

frame = tkinter.ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tkinter.NW)

class Chat:
    def __init__(self,frame,ind,send,msg,row):
        self.ind = ind
        self.send = send
        self.msg = msg
        self.frame = frame
        self.row = row

        label = ttk.Label(self.frame, text=f'index: {self.ind}, sender: {self.send}, message: {self.msg}')
        label.grid(row=self.row, column=0, padx=10, pady=5, sticky=tkinter.W)

        # del_key_button = tkinter.Button(frame, text="del", command=lambda: del_msg(d["index"]))
        del_button = tkinter.Button(self.frame, text="del")
        del_button.config(command=lambda : self.del_msg(self.ind))
        del_button.grid(row=self.row, column=1, padx=10, pady=5, sticky=tkinter.W)

    def del_msg(self,ind):
        del_msg(ind)
        # print(f'Delete called for : {ind}')


def del_msg(ind):
    # print(f'Delete called for : {ind}')
    fh.del_json_with_index(ind)
    myServer.send_json_array(fh.read_json_array())
    read_and_update_data()

def populate_frame(data):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Iterate over the JSON data and create labels for each key-value pair
    row = fh.get_len_of_json_array()
    for d in data:
        c = Chat(frame,d["index"], d["sender"],d["message"],row)
        row -= 1


# Function to read and update JSON data from file
def read_and_update_data():
    # Load the JSON data from a file (replace with your own JSON file)
    # nfh = fh("data.txt")
    data = fh.read_json_array()
    # Populate the frame with the JSON data
    populate_frame(data)

    # Update the scrollable area
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Schedule the next update after 1 second
    # window.after(100, read_and_update_data)

# Start the initial read and update process
read_and_update_data()

window.bind("<Return>", mesg_entered)

recv_thread = threading.Thread(target=meg_recv)
recv_thread.daemon = True
recv_thread.start()

window.mainloop()