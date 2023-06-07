import clip
from pynput import keyboard

app = clip.ClipBoard()


# with keyboard.GlobalHotKeys({'<ctrl>+<shift>+v': app.show_window}) as hotkeys:
with keyboard.GlobalHotKeys({'<cmd_l>+v': app.show_window}) as hotkeys:
    app.mainloop()
    hotkeys.join()