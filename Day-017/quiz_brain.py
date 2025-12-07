from question_model import Question
from data import question_data

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # checks if the quiz has ended or not
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # pull up the next question based on the question_number
    def next_question(self):
        cur_q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {cur_q.text} (True/False)?: ")
        self.check_answer(answer, cur_q.answer)

    def check_answer(self, ans, cor_ans):
        if ans.lower() == cor_ans.lower() :
            print("You got it right!")
            self.score += 1
        else :
            print("That is wrong")
        print(f"The correct answer was: {cor_ans} and now your new score is {self.score}/{self.question_number} ")
        print("\n")