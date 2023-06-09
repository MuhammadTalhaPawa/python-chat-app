import tkinter as tk
from tkinter import scrolledtext

chats = [
    {"index": 1, "sender": "Talha", "message": "Hellow how are you"},
    {"index": 2, "sender": "Talha", "message": "Where are you"},
    {"index": 3, "sender": "Saad",  "message": "I am fine how are you"},
    {"index": 4, "sender": "Talha", "message": "You f**king"},
    {"index": 5, "sender": "Saad",  "message": "You f**king f**king f**king"},
    {"index": 6, "sender": "Talha", "message": "Ok Bye"},
]


def submit_text():
    entered_text = text_entry.get()
    print("Entered text:", entered_text)

window = tk.Tk()
window.title("Server Window")

window.geometry(f"{600}x{400}")

# Create a label widget
label = tk.Label(window, text="Enter text:")
label.pack()

# Create a text entry widget
text_entry = tk.Entry(window,width=50)
text_entry.pack()

# Create a button widget
submit_button = tk.Button(window, text="Send", command=submit_text)
submit_button.pack()

def del_chat(index):
    # print("in del")
    print(f'Del chat index : {index}')

class Chat_Label:
    def __init__(self,win,ind,send,mes):
        self.label = tk.Label(win,text=f"{ind}: {send}: {mes}")
        self.del_but = tk.Button(win, text="x", command=lambda: del_chat(ind))

    def show(self):
        self.label.pack()
        self.del_but.pack()

for chat in chats:
    c = Chat_Label(window,chat['index'],chat['sender'],chat['message'])
    c.show()


# c1 = Chat_Label(window,1,"Talha","Hellow")
# c2 = Chat_Label(window,2,"Saad","Me Fine")
# c3 = Chat_Label(window,3,"Saad","How are you")

# c1.show()
# c2.show()
# c3.show()


# for chat in chats:
#     label1 = tk.Label(window,text=f"{chat['index']}: {chat['sender']}: {chat['message']}")
#     label1.pack()

#     del_button = tk.Button(window, text="del", command=lambda: del_chat(chat['index']))
#     del_button.pack()



# Start the main event loop
window.mainloop()
