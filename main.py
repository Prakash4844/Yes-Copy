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

# Create the root window
app = clip.ClipBoard()


def populate_clipboard():
    with open('clip.json') as file:
        data = json.load(file)
        rel_y = 0.1
        for clip in data['clip']:
            text_box = ctk.CTkTextbox(app, width=320, height=50)
            text_box.place(relx=0.5, rely=rel_y, anchor=tk.CENTER)
            text_box.configure(state="normal")
            text_box.delete("0.0", tk.END)
            text_box.configure(font=("Liberation Mono", 15))
            text_box.insert("0.0", clip)
            text_box.configure(state="disabled")
            text_box.update()
            copy_button = ctk.CTkButton(app, text="Copy", fg_color="green", hover_color="dark green",
                                        command=app.set_clip_head,
                                        height=10, width=10)
            copy_button.place(relx=0.85, rely=rel_y, anchor=tk.CENTER)
            rel_y += 0.14


with keyboard.GlobalHotKeys({'<cmd_l>+v': app.show_window}) as hotkeys:
    app.mainloop()
    hotkeys.join()
