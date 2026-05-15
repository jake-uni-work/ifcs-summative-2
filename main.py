import tkinter as tk

from constants import *

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg=WINDOW_BG_COLOUR)
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.geometry(f"{WINDOW_INIT_WIDTH}x{WINDOW_INIT_HEIGHT}")
        self.title("Quiz") # TODO: final name
        self.add_temporary_components() # TODO: remove
    
    def add_temporary_components(self):
        label = tk.Label(self, text="Hello World!", fg=TEXT_FG_COLOUR, bg=WINDOW_BG_COLOUR, font=(None, 40)) # type: ignore
        label.pack()

if __name__ == "__main__":
    root = QuizApp()
    root.mainloop()
    