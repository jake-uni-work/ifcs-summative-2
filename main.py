import tkinter as tk
from tkinter import messagebox
import sys
from typing import Optional

from constants import *
from validation import *
from file_handler import *

import screens


class QuizApp(tk.Tk):
    def __init__(self, question_file_name: str = "questions.csv") -> None:
        super().__init__()
        self.name: Optional[str] = None
        self.active_container: Optional[tk.Frame] = None
        self.questions: list[dict] = load_questions(question_file_name)
        self.score: int = 0
        self.scores: list[int] = []
        self.answers: list[str] = []
        
        # Cache the original exception handler so the error can still be printed to the console
        self.original_report_callback_exception = self.report_callback_exception
        self.report_callback_exception = self.handle_error

        self.config(bg=WINDOW_BG_COLOUR)
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.geometry(f"{WINDOW_INIT_WIDTH}x{WINDOW_INIT_HEIGHT}")
        self.title("Quiz")

        self.draw_welcome_screen()

    def draw_welcome_screen(self) -> None:
        """Clears the current view and displays the welcome screen"""
        self.clear_screen()
        self.active_container = screens.WelcomeScreen(self)
        self.active_container.pack(expand=True, fill="both")

    def draw_question(self, question_number: int):
        """Clears the current view and displays the provided question number"""
        self.clear_screen()
        self.active_container = screens.QuestionView(self, question_number)
        self.active_container.pack(expand=True, fill="both")

    def draw_end_screen(self):
        """Clears the current view and displays the ending screen, showing the results"""
        self.clear_screen()
        self.save_results()
        self.active_container = screens.EndView(self)
        self.active_container.pack(expand=True, fill="both")

    def save_results(self):
        if self.name is None:
            # this should never be called like this so an error can just be raised
            raise ValueError("Cannot save results without a name")

        save_results("results.csv", self.name, self.answers)

    def clear_screen(self):
        if self.active_container:
            self.active_container.destroy()
            self.active_container = None
        else:
            for elem in self.winfo_children():
                elem.destroy()
                
                
    def handle_error(self, exc, val, tb):
        self.original_report_callback_exception(exc, val, tb)
        messagebox.showerror(title="Error", message=f"A fatal error has occurred, program will now exit:\n{exc.__name__}: {val}")
        self.destroy()
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        root = QuizApp(sys.argv[1])
    else:
        root = QuizApp()
    root.mainloop()
