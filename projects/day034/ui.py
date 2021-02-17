from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.score_label = Label(bg=THEME_COLOR, fg="white", text="Score: 0")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text.",
            font=("Arial", 20, "italic")
        )
        self.false_button = Button(command=self.false_pressed, highlightthickness=0, image=false_image)
        self.true_button = Button(command=self.true_pressed, highlightthickness=0, image=true_image)

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, columnspan=2, pady=50, row=1)
        self.false_button.grid(column=1, row=2)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas["bg"] = "white"
        if self.quiz.still_has_questions():
            self.score_label["text"] = f"Score: {self.quiz.score}"
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas["bg"] = "green"
        else:
            self.canvas["bg"] = "red"
        self.window.after(1000, self.get_next_question)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
