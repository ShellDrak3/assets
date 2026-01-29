import tkinter as tk

# Main Window

root = tk.Tk()
root.title("Test")

# Windows Size

window_width = 300
window_height = 200

# Calculates width of device
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()

# Calculates correct dimensions for central fit
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# Main Message

message = tk.Label(root, text="Hello, World!")
message.pack()


root.mainloop()
