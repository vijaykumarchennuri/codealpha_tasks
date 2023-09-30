class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question = 0

    def add_question(self, question, correct_answer):
        self.questions.append({'question': question, 'answer': correct_answer})

    def display_next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            print(f"Question {self.current_question + 1}: {question_data['question']}")
            self.current_question += 1
        else:
            print("No more questions in the quiz.")

    def take_quiz(self):
        score = 0
        for question_data in self.questions:
            user_answer = input(f"Question {self.current_question}: {question_data['question']} ").strip()
            if user_answer.lower() == question_data['answer'].lower():
                score += 1
            self.current_question += 1
        print(f"Your score: {score}/{len(self.questions)}")

class Administrator:
    def __init__(self, quiz):
        self.quiz = quiz

    def create_quiz(self):
        while True:
            question = input("Enter a question (or 'q' to quit): ").strip()
            if question.lower() == 'q':
                break
            correct_answer = input("Enter the correct answer: ").strip()
            self.quiz.add_question(question, correct_answer)

def main():
    predefined_questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    }

    quiz = Quiz()

    for question, answer in predefined_questions.items():
        quiz.add_question(question, answer)

    while True:
        user_role = input("Are you an Administrator (A) or a User (U)? ").strip().lower()

        if user_role == 'a':
            administrator = Administrator(quiz)
            administrator.create_quiz()
        elif user_role == 'u':
            quiz.current_question = 0  # Reset the question counter for users
            while quiz.current_question < len(quiz.questions):
                quiz.display_next_question()
                input("Type the answer and press Enter to see the next question...")
            quiz.take_quiz()
        else:
            print("Invalid role. Please choose 'A' for Administrator or 'U' for User.")

        another_attempt = input("Do you want to try again? (yes/no): ").strip().lower()
        if another_attempt != 'yes':
            break

if __name__ == "__main__":
    main()
