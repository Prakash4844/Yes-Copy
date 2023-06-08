from customtkinter import *
import tkinter as tk
import pyperclip


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
        self.mouse_x = 0
        self.mouse_y = 0
        self.window_x = 0
        self.window_y = 0

    def populate_clipboard(self, target_tab, length):
        rel_y = 0.085
        scrollable_frame = CTkScrollableFrame(target_tab, width=320, height=390)
        scrollable_frame.pack()

        for clip_text in self.clip_data['clip']:
            button_1 = CTkButton(scrollable_frame, text=clip_text, fg_color="#272626",
                                 width=270,
                                 height=35,
                                 anchor="w",
                                 command=lambda: pyperclip.copy(clip_text))
            button_1.pack(pady=1, expand=True, fill="both")
            # copy_button = CTkButton(scrollable_frame, text="Copy", fg_color="blue",
            #                         hover_color="dark blue",
            #                         command=self.set_clip_head,
            #                         height=10, width=10)
            # copy_button.pack(anchor="e")
            # save_button = CTkButton(scrollable_frame, text="Save", fg_color="green",
            #                         hover_color="dark green",
            #                         command=self.set_clip_head,
            #                         height=10, width=10)
            # save_button.pack(anchor="e")

        # for clip_text in self.clip_data['clip']:
        #     text_box = CTkTextbox(scrollable_frame, width=300, height=35)
        #     text_box.place(relx=0.5, rely=rel_y, anchor=tk.CENTER)
        #     text_box.configure(state="normal")
        #     text_box.delete("0.0", tk.END)
        #     text_box.configure(font=("Liberation Mono", 12))
        #     text_box.insert("0.0", clip_text)
        #     text_box.configure(state="disabled")
        # text_box.update()
        # copy_button = CTkButton(self, master=target_tab, text="Copy", fg_color="green",
        #                         hover_color="dark green",
        #                         command=self.set_clip_head,
        #                         height=10, width=10)
        # copy_button.place(relx=0.85, rely=rel_y, anchor=tk.CENTER)
        # rel_y += 0.111

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

    def on_closing(self):
        self.withdraw()
