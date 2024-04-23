class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist

    def nextQuestion(self):
        ans = input(f"Q. {self.question_number} : {self.question_list[self.question_number].text} (True/False) ")