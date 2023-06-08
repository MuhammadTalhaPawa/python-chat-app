import tkinter as tk
from tkinter import scrolledtext
import json

def update_text():
    try:
        with open('data.json') as file:
            data = json.load(file)
            text_area.delete('1.0', tk.END)  # Clear the text area
            text_area.insert(tk.END, json.dumps(data, indent=4))  # Update the text area with JSON data
    except FileNotFoundError:
        text_area.delete('1.0', tk.END)  # Clear the text area if file is not found
        text_area.insert(tk.END, "File not found.")

window = tk.Tk()
window.title("JSON File Update Example")

window_width = 600
window_height = 400

# Set the window dimensions
window.geometry(f"{window_width}x{window_height}")

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Text widget
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_area.pack()

# Create a button to update the text area
update_button = tk.Button(window, text="Update", command=update_text)
update_button.pack()

# Configure the Scrollbar to scroll the Text widget
scrollbar.config(command=text_area.yview)

# Start the main event loop
window.mainloop()
