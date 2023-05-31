import tkinter as tk
import CTkMessagebox
import customtkinter as ctk
import pyperclip as pyclip
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

clip_history_length = config["APP"]["HISTORY_LENGTH"]
win_shortcut = config["APP"]["WINDOW_SHORTCUT"]

ctk.set_appearance_mode("System")  # Set appearance mode to system
ctk.set_default_color_theme("blue")  # Set default color theme to blue

# Create the root window
app = ctk.CTk()  # create CTk window like you do with the Tk window
# Hide the window initially
app.withdraw()

app.geometry("350x400")
app.resizable(False, False)
app.title("Yes Copy")
# Remove the window decoration
app.overrideredirect(True)

# Get the current mouse position
mouse_x = app.winfo_pointerx()
mouse_y = app.winfo_pointery()

# Calculate the window position relative to the mouse
window_x = mouse_x - app.winfo_width() // 2
window_y = mouse_y - app.winfo_height() // 2

# Set the window position
app.geometry(f"+{window_x}+{window_y}")

# Show the window
app.deiconify()

app.mainloop()
