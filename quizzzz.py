import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.score = 0
        self.current_question = 0

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(expand=True, fill="both")

        self.question_label = tk.Label(self.main_frame, text="", font=('Arial', 14))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.inner_frame = tk.Frame(self.main_frame)
        self.inner_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.option_var = tk.IntVar()
        self.option_var.set(-1) 

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.inner_frame, text="", variable=self.option_var, value=i)
            button.grid(row=i, column=0, pady=5, sticky='w')

            self.option_buttons.append(button)

        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_answer)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.play_again_button = tk.Button(self.main_frame, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question['text'])

            for i, option in enumerate(question['options']):
                self.option_buttons[i].config(text=option)

            self.submit_button.config(state=tk.NORMAL)
        else:
            self.show_result()

    def submit_answer(self):
        selected_option = self.option_var.get()

        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option!")
        else:
            correct_option = self.questions[self.current_question]['correct_option']

            if selected_option == correct_option:
                messagebox.showinfo("Feedback", "Correct!")
                self.score += 1
            else:
                correct_option_text = self.questions[self.current_question]['options'][correct_option]
                messagebox.showinfo("Feedback", f"Wrong! The correct answer was: {correct_option_text}")

            self.current_question += 1
            self.option_var.set(-1)  

            if self.current_question < len(self.questions):
                self.display_question()
            else:
                self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")
        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.current_question = 0
        self.score = 0
        self.submit_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.display_question()



questions = [
    {
       'text': 'How many planets are present in the solar system?',
        'options': ['Eight', 'Nine', 'Seven', 'Ten'],
        'correct_option': 0
    },
    {
        'text': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_option': 0
    },
    {
        'text': 'How many continents are there on earth?',
        'options': ['Eight', 'Nine', 'Seven', 'Ten'],
        'correct_option': 2
    }
]

root = tk.Tk()
root.title("Quiz App")
root.state('zoomed')
root.configure(bg="green")
root.geometry("400x400")  
quiz_app = QuizApp(root, questions)
root.mainloop()
