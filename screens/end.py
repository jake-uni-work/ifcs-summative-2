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
        self.parent = parent
        header_label = tk.Label(self, text="Your results", font=font(30), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        header_label.pack(pady=(20, 0))

        score_label = tk.Label(
            self, text=f"You scored {parent.score}/{len(parent.questions)}", font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR)
        score_label.pack(pady=(20, 0))

        strongest, weakest = self.calculate_categories()

        strongest_label = tk.Label(
            self, text=f"Your strongest categories were:", font=font(25), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
        )
        strongest_label.pack(pady=(20, 0))

        strongest_3_text_label = tk.Label(
            self, text=", ".join(strongest), font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
        )
        strongest_3_text_label.pack(pady=(0, 20))

        weakest_3_label = tk.Label(
            self, text=f"Your weakest categories were:", font=font(25), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
        )
        weakest_3_label.pack(pady=(20, 0))

        weakest_3_text_label = tk.Label(
            self, text=", ".join(weakest), font=font(20), bg=WINDOW_BG_COLOUR, fg=TEXT_FG_COLOUR
        )
        weakest_3_text_label.pack(pady=(0, 20))

    def calculate_categories(self):
        return strongest_and_weakest_by_category(calculate_categories(self.parent.questions, self.parent.score_by_question))


def determine_count(categories: int) -> int:
    if 0 <= categories <= 3:
        return 1
    elif 4 <= categories < 8:
        return 2
    else:
        return 3


def strongest_and_weakest_by_category(score_by_category: dict[str, int]):
    sorted_list = [tuple_[0] for tuple_ in sorted(
        [(category, score) for category, score in score_by_category.items()], key=lambda tuple_: tuple_[1])]
    count = determine_count(len(score_by_category))
    if count == 1:
        strongest = [sorted_list[-1]]
        weakest = [sorted_list[0]]
    else:
        strongest = list(reversed(sorted_list[-count:]))
        weakest = sorted_list[0:count]

    return (strongest, weakest)


def calculate_categories(questions: list[dict], scores: dict[int, int]):
    score_by_category: dict[str, int] = {}
    for idx, question in enumerate(questions):
        question_number = idx + 1
        category = question.get("category", None)
        if category:
            score_by_category.setdefault(category, 0)
            if scores[question_number] > 0:
                score_by_category[category] += 1

    return score_by_category
