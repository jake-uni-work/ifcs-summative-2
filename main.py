import tkinter as tk
from tkinter import messagebox
from typing import Optional

from constants import *
from validation import *

# TODO: extract into own file?
class WelcomeScreen(tk.Frame):
    def __init__(self, parent: "QuizApp"):
        self.parent = parent
        super().__init__(parent, bg=WINDOW_BG_COLOUR)
        welcome_label = tk.Label(self, text="Welcome to the Quiz", bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR, font=font(27))
        welcome_label.pack(pady=(45, 0))
        
        enter_name_label = tk.Label(self, text="Enter your name below to begin", bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR, font=font(19))
        enter_name_label.pack(pady=(50, 0))
        self.name_var = tk.StringVar(self)
        enter_name_input = tk.Entry(self, font=font(12), width=50, textvariable=self.name_var)
        enter_name_input.pack(pady=(1, 0))
        
        begin_button = tk.Button(self, width=5, height=2, text="Begin\nQuiz", font=font(20), command=self.begin_quiz)
        begin_button.pack(pady=(100, 0))
        
    def begin_quiz(self):
        entered_name = format_name(self.name_var.get())
        if not entered_name:
            messagebox.showerror(title="Error", message="You must enter a name.")       
        elif not validate_name_length(entered_name):
            messagebox.showerror(title="Error", message="Name must be between 3 and 50 characters.")
        elif not validate_name_characters(entered_name):
            messagebox.showerror(title="Error", message="Name must contain only letters, spaces, hyphens, and apostraphes.")
        else:
            # TODO: questions
            ...
               

class QuizApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.config(bg=WINDOW_BG_COLOUR)
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.geometry(f"{WINDOW_INIT_WIDTH}x{WINDOW_INIT_HEIGHT}")
        self.title("Quiz") # TODO: final name
        self.active_container: Optional[tk.Frame] = None
        self.draw_welcome_screen()

    def draw_welcome_screen(self) -> None:
        self.clear_screen()
        # TODO: extract into own class
        self.active_container = WelcomeScreen(self)
        self.active_container.pack(expand=True, fill="both")

    def clear_screen(self):
        if self.active_container:
            for elem in self.active_container.winfo_children():
                elem.destroy()
            self.active_container.destroy()
            self.active_container = None
        else:
            for elem in self.winfo_children():
                elem.destroy()

if __name__ == "__main__":
    root = QuizApp()
    root.mainloop()
    