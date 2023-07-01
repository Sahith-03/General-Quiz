from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.window.minsize(width=350,height=500)

        self.score_label = Label(text=f"Score: {self.score}",bg=THEME_COLOR,font=("Arial",15),foreground="white")
        self.score_label.grid(row=0,column=1,padx=20)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,width=280,text="Hi",font=("Arial",17,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        tick = PhotoImage(file="images/true.png")
        self.right = Button(image=tick,command=self.true_pressed)
        self.right.grid(row=2,column=0)

        cross = PhotoImage(file="images/false.png")
        self.wrong = Button(image=cross,command=self.false_pressed)
        self.wrong.grid(row=2, column=1,pady=40)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions() == True:
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.score_label.destroy()
            self.right.destroy()
            self.wrong.destroy()
            self.canvas.itemconfig(self.question,text=f"Score: {self.quiz.score}",font=("Arial",40,"italic"))
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
