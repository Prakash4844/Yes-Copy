from customtkinter import *
from tkinter import *


class ClipBoard(CTk):
    def __init__(self):
        super().__init__()
        self.title("Yes Copy")
        self.geometry("350x400")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.withdraw()
        self.my_frame = CTkScrollableFrame(master=self, width=320, height=390)
        self.my_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.mouse_x = 0
        self.mouse_y = 0
        self.window_x = 0
        self.window_y = 0

    def show_window(self):
        # Get the current mouse position
        self.mouse_x = self.winfo_pointerx()
        self.mouse_y = self.winfo_pointery()

        # Calculate the window position relative to the mouse
        self.window_x = self.mouse_x - self.winfo_width() // 2
        self.window_y = self.mouse_y - self.winfo_height() // 2

        self.geometry(f"+{self.window_x}+{self.window_y}")
        self.deiconify()
        # populate_clipboard()

    def on_closing(self):
        self.withdraw()

    def set_clip_head(self):
        pass
