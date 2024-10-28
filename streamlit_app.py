import tkinter as tk

class QuizzoneApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quizzone")
        self.geometry("400x300")

        # Introduction screen
        self.intro_frame = tk.Frame(self)
        self.intro_label = tk.Label(self.intro_frame, text="Welcome to Quizzone!")
        self.intro_image = tk.PhotoImage(file="quizzone_logo.png")  # Replace with your image path
        self.intro_image_label = tk.Label(self.intro_frame, image=self.intro_image)
        self.start_button = tk.Button(self.intro_frame, text="Start Quiz", command=self.start_quiz)

        self.intro_label.pack(pady=20)
        self.intro_image_label.pack()
        self.start_button.pack(pady=20)
        self.intro_frame.pack(fill="both", expand=True)

        # Question screen
        self.question_frame = tk.Frame(self)
        self.question_label = tk.Label(self.question_frame, text="Question 1: Placeholder Question")
        self.answer_var = tk.StringVar()
        self.answer_options = [
            ("Option A", "A"),
            ("Option B", "B"),
            ("Option C", "C"),
            ("Option D", "D")
        ]
        self.answer_buttons = []
        for text, value in self.answer_options:
            button = tk.Radiobutton(self.question_frame, text=text, variable=self.answer_var, value=value)
            button.pack(anchor="w")
            self.answer_buttons.append(button)
        self.feedback_label = tk.Label(self.question_frame, text="")
        self.next_button = tk.Button(self.question_frame, text="Next", state="disabled", command=self.next_question)

        # Hide question frame initially
        self.question_frame.pack_forget()

    def start_quiz(self):
        self.intro_frame.pack_forget()
        self.question_frame.pack(fill="both", expand=True)
        self.show_question(0)  # Start with question 0

    def show_question(self, question_index):
        # Update question and answer options
        self.question_label.config(text=f"Question {question_index+1}: Placeholder Question {question_index+1}")
        for i, (text, value) in enumerate(self.answer_options):
            self.answer_buttons[i].config(text=text, value=value)

        # Enable answer buttons and disable next button
        for button in self.answer_buttons:
            button.config(state="normal")
        self.next_button.config(state="disabled")

    def check_answer(self):
        # Check if the selected answer is correct
        correct_answer = "A"  # Replace with the actual correct answer
        if self.answer_var.get() == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. The correct answer is A.", fg="red")
        self.next_button.config(state="normal")

    def next_question(self):
        # Disable answer buttons
        for button in self.answer_buttons:
            button.config(state="disabled")
        self.feedback_label.config(text="")

        # Show the next question or end the quiz
        if question_index < len(questions) - 1:
            self.show_question(question_index + 1)
        else:
            # End the quiz, display a final score or message
            pass

if __name__ == "__main__":
    app = QuizzoneApp()
    app.mainloop()
