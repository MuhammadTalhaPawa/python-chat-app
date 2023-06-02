import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Client 1")

# Set the window dimensions
window.geometry("400x300")

# Add a label to the window
label = tk.Label(window, text="Hello, World!")
label.pack()

# Run the main window loop
window.mainloop()
