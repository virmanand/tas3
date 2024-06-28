class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
            {"question": "Which programming language is this quiz written in?", "answer": "Python"},
            {"question": "What is the largest living species of lizard?", "answer": "Komodo dragon"},
            {"question": "What is the chemical symbol for gold?", "answer": "Au"}
        ]
        self.score = 0

    def ask_question(self, question):
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {question['answer']}")

    def run_quiz(self):
        for question in self.questions:
            self.ask_question(question)
        print(f"Your final score is {self.score} out of {len(self.questions)}")


if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()