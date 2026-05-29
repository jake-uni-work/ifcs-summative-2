import tkinter as tk
import sys
from typing import Optional
from datetime import datetime

from constants import *
from validation import *
from question_loader import *

import screens


class QuizApp(tk.Tk):
    def __init__(self, question_file_name: str = "questions.csv") -> None:
        super().__init__()
        self.name: Optional[str] = None
        self.active_container: Optional[tk.Frame] = None
        self.questions: list[dict] = load_questions(question_file_name)
        self.score: int = 0
        # TODO: store in a list instead
        self.score_by_question: dict[int, int] = {}
        self.answer_by_question: dict[int, str] = {}

        self.config(bg=WINDOW_BG_COLOUR)
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.geometry(f"{WINDOW_INIT_WIDTH}x{WINDOW_INIT_HEIGHT}")
        self.title("Quiz")  # TODO: final name

        self.draw_welcome_screen()

    def draw_welcome_screen(self) -> None:
        self.clear_screen()
        self.active_container = screens.WelcomeScreen(self)
        self.active_container.pack(expand=True, fill="both")

    def draw_question(self, question_number: int):
        self.clear_screen()
        self.active_container = screens.QuestionView(self, question_number)
        self.active_container.pack(expand=True, fill="both")

    def draw_end_screen(self):
        self.clear_screen()
        self.save_results()
        self.active_container = screens.EndView(self)
        self.active_container.pack(expand=True, fill="both")

    def save_results(self):
        # TODO move
        file_name = "results.csv"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        answers: list[str] = []

        # TODO: must be a list not a dict this is really ugly
        for key in sorted(self.answer_by_question.keys()):
            answers.append(self.answer_by_question[key])

        with open(file_name, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([now, self.name, answers])

    def clear_screen(self):
        if self.active_container:
            self.active_container.destroy()
            self.active_container = None
        else:
            for elem in self.winfo_children():
                elem.destroy()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # TODO: proper error handling
        root = QuizApp(sys.argv[1])
    else:
        root = QuizApp()
    root.mainloop()
