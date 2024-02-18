import tkinter as tk
from tkinter import ttk

class TransparentWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        button_color = ('#00ff00')
        self.config(bg='white')  # set background color to white
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.geometry("+{}+{}".format(
            0,  # set x position to the right of the screen ##self.winfo_screenwidth()
            # set y position to the middle of the screen
            self.winfo_screenheight() // 2 - 170
        ))

        self.attributes("-alpha", 1)  # set transparency to 70%
        # set transparent color to white
        self.attributes("-transparentcolor", "white")
        self.overrideredirect(True)  # remove window border and title bar

        self.bind("<FocusOut>", self.on_focus_out)


    def add_button(self, text, command):
        button = tk.Button(self, text=text, width=20, height=3, command=command
                           ,borderwidth=0, highlightthickness=0, bg="#040f13", fg="#08d7ff", relief="flat"
                           , activebackground="#08d7ff", activeforeground="#040f13"
                           , cursor='hand2', font=('Arial', 12, 'bold'))
        button.pack(pady=2)

    def on_closing(self):
        self.attributes("-alpha", 0.5)

    def on_focus_out(self, event):
        # Bring the window back to the front when it loses focus
        self.attributes("-topmost", True)

    def close_window(self):
        self.destroy()

