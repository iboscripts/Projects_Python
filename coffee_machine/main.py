from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

"""for question in question_data:
    each_question = Question(question['text'], question['answer'])
    question_bank.append(each_question)

print(question_bank)"""

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    each_question = Question(text, answer)
    question_bank.append(each_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

