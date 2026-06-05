import tkinter as tk

from constants import *
from functools import partial

# The below code will get around a circular import so that type hinting works properly
# TYPE_CHECKING is always False at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import QuizApp

class QuestionView(tk.Frame):
    """Displays a singular question"""
    def __init__(self, parent: "QuizApp", question_number: int) -> None:
        super().__init__(
            parent,
            bg=WINDOW_BG_COLOUR
        )
        self.parent = parent
        self.question_number = question_number
        self.question = self.parent.questions[self.question_number - 1]
        self.answer_buttons: dict[str, tk.Button] = {}
        self.score_label = None
        self.draw_header()
        self.draw_question()
        self.draw_answers()

    def draw_header(self):
        """Draws the header of the window containing the question number and the score"""
        header_frame = tk.Frame(
            self,
            bg=WINDOW_BG_COLOUR
        )
        header_frame.pack(fill="x")

        question_num_label = tk.Label(
            header_frame,
            text=f"Question {self.question_number} of {len(self.parent.questions)}",
            font=font(25),
            bg=WINDOW_BG_COLOUR,
            wraplength=640,
            justify="center"
        )
        question_num_label.pack(anchor="nw", side="left")

        self.score_label = tk.Label(
            header_frame,
            text=f"Score: {self.parent.score}/{self.question_number - 1}",
            font=font(25),
            bg=WINDOW_BG_COLOUR
        )
        self.score_label.pack(anchor="ne", side="right")

    def draw_question(self):
        """Draws the actual question text"""
        question_text_label = tk.Label(
            self,
            text=self.question['question'],
            font=font(15),
            wraplength=self.winfo_width(),
            justify="left",
            bg=WINDOW_BG_COLOUR
        )
        question_text_label.pack(fill="x", pady=(0, 20))

        # Automatically update the text wrap size when the window is resized
        self.bind('<Configure>', lambda _: question_text_label.configure(wraplength=self.winfo_width()))

    def draw_answers(self):
        """Draws the answer buttons"""
        for option in ("a", "b", "c", "d"):
            # Using a lambda function here causes the option to always be "d", so use a functools partial instead which does work properly
            command = partial(self.on_answer_click, option)
            answer_button = tk.Button(self, text=f"{option.upper()}: {self.question['options'][option]}", font=font(20), width=35, command=command)
            answer_button.pack(pady=(0, 20))
            self.answer_buttons[option] = answer_button

    def on_answer_click(self, option: str) -> None:
        """
        Callback when any answer button is clicked.
        
        This function will check whether the answer is correct, and update the UI accordingly.
        
        Args:
            option: the option that is clicked
                    
        """
        for btn in self.answer_buttons.values():
            btn.configure(state="disabled", command=lambda: ...)
            
        self.parent.answers.append(option)
        # TODO: extract answer checking logic from UI update logic to ensure it can be tested
        correct = self.question['correct']
        if option == correct:
            self.answer_buttons[option].configure(bg="green", disabledforeground="black")
            self.parent.score += 1
            self.parent.scores.append(1)
        else:
            self.answer_buttons[option].configure(bg="red", disabledforeground="black")
            self.answer_buttons[correct].configure(bg="green", disabledforeground="black")
            self.parent.scores.append(0)

        if self.score_label:
            self.score_label.configure(text=f"Score: {self.parent.score}/{self.question_number}")
            
        next_question_button = tk.Button(
            self,
            width=8,
            height=2,
            text="Finish\nQuiz" if self.question_number >= len(self.parent.questions) else "Next\nQuestion",
            font=font(20),
            command=self.draw_next_question
        )
        next_question_button.pack(pady=(0, 0), side="bottom")
        
    def draw_next_question(self):
        """If this question is the last question, this will draw the end screen. Otherwise, it will draw the next question"""
        if self.question_number >= len(self.parent.questions):
            self.parent.draw_end_screen()
        else:
            self.parent.draw_question(self.question_number + 1)