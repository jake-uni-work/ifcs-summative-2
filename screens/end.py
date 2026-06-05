import tkinter as tk

from constants import *
from category_calculation import *

# The below code will get around a circular import so that type hinting works properly
# TYPE_CHECKING is always False at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import QuizApp


class EndView(tk.Frame):
    """The ending screen.
    
    Shows the results of the quiz and strongest and weakest categories"""
    def __init__(self, parent: "QuizApp"):
        super().__init__(parent, bg=WINDOW_BG_COLOUR)
        self.parent = parent
        header_label = tk.Label(self, text="Your results", font=font(30), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        header_label.pack(pady=(20, 0))

        score_label = tk.Label(
            self, text=f"You scored {parent.score}/{len(parent.questions)}", font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        score_label.pack(pady=(20, 0))

        strongest, weakest = self.calculate_categories()
        if strongest:
            strongest_label = tk.Label(
                self, text=f"Your strongest categories were:", font=font(25), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
            )
            strongest_label.pack(pady=(20, 0))

            strongest_3_text_label = tk.Label(
                self, text=", ".join(strongest), font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
            )
            strongest_3_text_label.pack(pady=(0, 20))
        if weakest:
            weakest_3_label = tk.Label(
                self, text=f"Your weakest categories were:", font=font(25), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
            )
            weakest_3_label.pack(pady=(20, 0))

            weakest_3_text_label = tk.Label(
                self, text=", ".join(weakest), font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
            )
            weakest_3_text_label.pack(pady=(0, 20))

    def calculate_categories(self):
        return strongest_and_weakest_categories(calculate_categories(self.parent.questions, self.parent.scores))
