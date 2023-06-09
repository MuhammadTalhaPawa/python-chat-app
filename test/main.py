import tkinter as tk
from tkinter import ttk
import json
import time
from file_handler import File_Handler as fh

# Create the Tkinter window
window = tk.Tk()
window.title("Dynamic JSON Viewer")

# Create a scrollable frame
scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=canvas.yview)

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Function to populate the frame with JSON data
def populate_frame(data):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Iterate over the JSON data and create labels for each key-value pair
    row = 0
    for d in data:
        key_label = ttk.Label(frame, text=f'index: {d["index"]}, sender: {d["sender"]}, message: {d["message"]}, ')
        key_label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)

        row += 1

# Function to read and update JSON data from file
def read_and_update_data():
    # Load the JSON data from a file (replace with your own JSON file)
    nfh = fh("data.txt")
    data = nfh.read_json_array()
    # Populate the frame with the JSON data
    populate_frame(data)

    # Update the scrollable area
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Schedule the next update after 1 second
    window.after(1000, read_and_update_data)

# Start the initial read and update process
read_and_update_data()

# Start the Tkinter event loop
window.mainloop()
