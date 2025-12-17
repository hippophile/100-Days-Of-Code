from turtle import Turtle

class Scoreboard(Turtle):
    score = 0 

    def __init__(self):
        super().__init__()
        self.ht()
        
    def refresh_score(self):
        self.reset()
        self.ht()
        self.penup
        self.goto(0, 250)
        self.color("gold")

        self.score += 1
        text = f"Score: {self.score}"
        self.write(text, align="center", font=('Arial', 24, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.color("gold")
        text = f"Game Over\n   Score: {Scoreboard.score}"
        self.write(text, align="center", font=('Arial', 28, 'normal'))


    