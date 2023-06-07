from customtkinter import *
import tkinter as tk


class ClipBoard(CTk):
    def __init__(self, data):
        super().__init__()
        self.clip_data = data
        set_appearance_mode("System")  # Set appearance mode to system
        set_default_color_theme("blue")  # Set default color theme to blue
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
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def populate_clipboard(self):
        rel_y = 0.1
        for clip_text in self.clip_data['clip']:
            text_box = CTkTextbox(self, width=310, height=50)
            text_box.place(relx=0.5, rely=rel_y, anchor=tk.CENTER)
            text_box.configure(state="normal")
            text_box.delete("0.0", tk.END)
            text_box.configure(font=("Liberation Mono", 15))
            text_box.insert("0.0", clip_text)
            text_box.configure(state="disabled")
            text_box.update()
            copy_button = CTkButton(self, text="Copy", fg_color="green",
                                    hover_color="dark green",
                                    command=self.set_clip_head,
                                    height=10, width=10)
            copy_button.place(relx=0.85, rely=rel_y, anchor=tk.CENTER)
            rel_y += 0.14

    def set_clip_head(self):
        pass

    def show_window(self):
        # Get the current mouse position
        self.mouse_x = self.winfo_pointerx()
        self.mouse_y = self.winfo_pointery()

        # Calculate the window position relative to the mouse
        self.window_x = self.mouse_x - self.winfo_width() // 2
        self.window_y = self.mouse_y - self.winfo_height() // 2

        self.geometry(f"+{self.window_x}+{self.window_y}")
        self.deiconify()
        self.populate_clipboard()

    def on_closing(self):
        self.withdraw()
