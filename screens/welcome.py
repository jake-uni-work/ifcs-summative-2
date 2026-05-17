import tkinter as tk
from tkinter import messagebox

from constants import *
from validation import *

# The below code will get around a circular import so that type hinting works properly
# TYPE_CHECKING is always False at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import QuizApp


class WelcomeScreen(tk.Frame):
    """The initial welcome screen which asks a player for their name, validates it, and then asks the first question"""

    def __init__(self, parent: QuizApp):
        self.parent = parent
        super().__init__(parent, bg=WINDOW_BG_COLOUR)
        welcome_label = tk.Label(
            self,
            text="Welcome to the Quiz",
            bg=WINDOW_BG_COLOUR,
            fg=TEXT_FG_COLOUR,
            font=font(27)
        )
        welcome_label.pack(pady=(45, 0))

        enter_name_label = tk.Label(
            self,
            text="Enter your name below to begin",
            bg=WINDOW_BG_COLOUR,
            fg=TEXT_FG_COLOUR,
            font=font(19)
        )
        enter_name_label.pack(pady=(50, 0))

        self.name_var = tk.StringVar(self)
        enter_name_input = tk.Entry(
            self,
            font=font(12),
            width=50,
            textvariable=self.name_var
        )
        enter_name_input.pack(pady=(1, 0))

        begin_button = tk.Button(
            self,
            width=5,
            height=2,
            text="Begin\nQuiz",
            font=font(20),
            command=self.begin_quiz
        )
        begin_button.pack(pady=(100, 0))

    def begin_quiz(self):
        entered_name = format_name(self.name_var.get())
        if not entered_name:
            messagebox.showerror(
                title="Error",
                message="You must enter a name."
            )
        elif not validate_name_length(entered_name):
            messagebox.showerror(
                title="Error",
                message="Name must be between 3 and 50 characters."
            )
        elif not validate_name_characters(entered_name):
            messagebox.showerror(
                title="Error",
                message="Name must contain only letters, spaces, hyphens, and apostraphes."
            )
        else:
            self.parent.name = entered_name
            self.parent.draw_question(1)
