import tkinter
from tkinter import ttk
import file_handler
import threading
from connection import Connection 

chatData = []

myClient = Connection()
myClient.init_as_client()

window = tkinter.Tk()
window.title("client Window")
window.geometry("400x300")

def mesg_entered(a = None):
    msg = enter_message_text.get()
    if msg == "":
        return
    enter_message_text.delete(0, tkinter.END)
    print(f'Entered text: {msg}')

    myClient.send_mesg(msg)
    
def meg_recv():
    while True:
        recv_json_array = myClient.recv_json_array()
        chatData.clear()
        for d in recv_json_array:
            chatData.append(d)
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
        print(f'Delete called for : {ind}')


def del_msg(ind):
    myClient.send_mesg(f'DELETE:{ind}')

def populate_frame(data):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Iterate over the JSON data and create labels for each key-value pair
    row = len(chatData)-1
    for d in chatData:
        c = Chat(frame,d["index"], d["sender"],d["message"],row)
        row -= 1


# Function to read and update JSON data from file
def read_and_update_data():
    # Load the JSON data from a file (replace with your own JSON file)
    # nfh = fh("data.txt")
    # Populate the frame with the JSON data
    populate_frame(chatData)

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