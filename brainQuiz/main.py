from data import question_data
from question_model import Quiz
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append(Quiz(questions["text"], questions["answer"]))

quiz = QuizBrain(question_bank)
quiz.nextQuestion()