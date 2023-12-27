class Quiz:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']
        print(f"\n{question}\nOptions: {', '.join(options)}")

    def get_user_input(self):
        return input("Your answer: ").strip().lower()

    def check_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['correct_answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    def run_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_input()

            while user_answer not in self.questions[i]['options']:
                print("Invalid option. Please choose from the provided options.")
                user_answer = self.get_user_input()

            self.check_answer(i, user_answer)

        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")


# Example quiz setup
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['a. Paris', 'b. Rome', 'c. Berlin'],
        'correct_answer': 'a'
    },
    {
        'question': 'Which programming language is known for its readability?',
        'options': ['a. Python', 'b. Java', 'c. C++'],
        'correct_answer': 'a'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['a. Elephant', 'b. Blue Whale', 'c. Giraffe'],
        'correct_answer': 'b'
    }
]

# Create and run the quiz
my_quiz = Quiz(quiz_questions)
my_quiz.run_quiz()
