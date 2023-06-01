import json
import tkinter as tk
import CTkMessagebox
import customtkinter as ctk
import pyperclip
import yaml
from pynput import keyboard

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

clip_history_length = config["APP"]["HISTORY_LENGTH"]
win_shortcut = config["APP"]["WINDOW_SHORTCUT"]

ctk.set_appearance_mode("System")  # Set appearance mode to system
ctk.set_default_color_theme("blue")  # Set default color theme to blue

# Create the root window
app = ctk.CTk()  # create CTk window like you do with the Tk window
app.resizable(False, False)
app.title("Yes Copy")
app.geometry("350x400")
app.protocol("WM_DELETE_WINDOW", app.iconify)
app.withdraw()
app.my_frame = ctk.CTkScrollableFrame(master=app, width=320, height=390)
app.my_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

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
            copy_button = ctk.CTkButton(app, text="Copy", fg_color="green" , hover_color="dark green",
                                        command=set_clip_head,
                                        height=10, width=10)
            copy_button.place(relx=0.85, rely=rel_y, anchor=tk.CENTER)
            rel_y += 0.14


def show_window():
    # Get the current mouse position
    mouse_x = app.winfo_pointerx()
    mouse_y = app.winfo_pointery()

    # Calculate the window position relative to the mouse
    window_x = mouse_x - app.winfo_width() // 2
    window_y = mouse_y - app.winfo_height() // 2

    app.geometry(f"+{window_x}+{window_y}")
    app.deiconify()
    populate_clipboard()


# Register the Ctrl+Shift+V combination
with keyboard.GlobalHotKeys({'<ctrl>+<shift>+v': show_window}) as hotkeys:
    app.mainloop()
    hotkeys.join()
