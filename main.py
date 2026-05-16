import tkinter as tk
from tkinter import messagebox
from typing import Optional
from functools import partial

from constants import *
from validation import *
from question_loader import *


class WelcomeScreen(tk.Frame):
    """The initial welcome screen which asks a player for their name, validates it, and then asks the first question"""
    def __init__(self, parent: "QuizApp"):
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
            answer_button = tk.Button(self, text=f"{option.upper()}: {self.question['options'][option]}", font=font(20), width=35, command=partial(self.on_answer_click, option))
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
            
        
        if self.question['category']:
            if self.question['category'] not in self.parent.score_by_category:
                self.parent.score_by_category[self.question['category']] = {"score": 0, "questions": 0}
        self.parent.score_by_category[self.question['category']]['questions'] += 1
        
        # TODO: extract answer checking logic from UI update logic to ensure it can be tested
        correct = self.question['correct']
        if option == correct:
            self.answer_buttons[option].configure(bg="green", disabledforeground="black")
            self.parent.score += 1
            if self.question['category']:
                self.parent.score_by_category[self.question['category']]['score'] += 1
        else:
            self.answer_buttons[option].configure(bg="red", disabledforeground="black")
            self.answer_buttons[correct].configure(bg="green", disabledforeground="black")
            
        if self.score_label:
            self.score_label.configure(text=f"Score: {self.parent.score}/{self.question_number}")
            
        next_question_button = tk.Button(
            self,
            width=8,
            height=2,
            text="Next\nQuestion",
            font=font(20),
            command=self.draw_next_question
        )
        next_question_button.pack(pady=(0, 0))
        
    def draw_next_question(self):
        self.parent.draw_question(self.question_number + 1)


class QuizApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.config(bg=WINDOW_BG_COLOUR)
        self.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.geometry(f"{WINDOW_INIT_WIDTH}x{WINDOW_INIT_HEIGHT}")
        self.title("Quiz")  # TODO: final name
        self.active_container: Optional[tk.Frame] = None
        self.questions = load_questions("questions.csv")
        self.draw_welcome_screen()
        self.score: int = 0
        self.score_by_category: dict[str, dict[str, int]] = {}
        self.name: Optional[str] = None

    def draw_welcome_screen(self) -> None:
        self.clear_screen()
        self.active_container = WelcomeScreen(self)
        self.active_container.pack(expand=True, fill="both")

    def draw_question(self, question_number: int):
        self.clear_screen()
        self.active_container = QuestionView(self, question_number)
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
