import tkinter as tk

from constants import *

# The below code will get around a circular import so that type hinting works properly
# TYPE_CHECKING is always False at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import QuizApp

class EndScreen(tk.Frame):
    def __init__(self, parent: "QuizApp"):
        super().__init__(parent, bg=WINDOW_BG_COLOUR)
        header_label = tk.Label(self, text="Your results", font=font(30), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        header_label.pack(pady=(20, 0))
        
        score_label = tk.Label(self, text=f"You scored {parent.score}/{len(parent.questions)}", font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        score_label.pack(pady=(20, 0))