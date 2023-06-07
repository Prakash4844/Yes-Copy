import json
import tkinter as tk
import CTkMessagebox
import customtkinter as ctk
import pyperclip
import yaml
from pynput import keyboard
import clip

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

clip_history_length = config["APP"]["HISTORY_LENGTH"]
win_shortcut = config["APP"]["WINDOW_SHORTCUT"]

ctk.set_appearance_mode("System")  # Set appearance mode to system
ctk.set_default_color_theme("blue")  # Set default color theme to blue

with open('clip.json') as file:
    data = json.load(file)


# Create the root window
app = clip.ClipBoard(data)


with keyboard.GlobalHotKeys({'<cmd_l>+v': app.show_window}) as hotkeys:
    app.mainloop()
    hotkeys.join()
