from turtle import Turtle

COLOR = "gold"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        
    def refresh_score(self):
        self.clear()
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.color(COLOR)

        self.score += 1
        text = f"Score: {self.score}"
        self.write(text, align="center", font=('Arial', 24, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.color("gold")
        text = f"Game Over\n   Score: {self.score}"
        self.write(text, align="center", font=('Arial', 28, 'normal'))

        file = open("high_score.txt", "r")
        HIGH_SCORE = file.read()
        file.close()  
        if self.score > int(HIGH_SCORE):
            self.goto(0, 150)
            text_hs = f"Wow New High Score: {self.score}"
            self.write(text_hs, align="center", font=('Arial', 28, 'normal'))
            HIGH_SCORE = self.score
            file = open("high_score.txt", "w")
            file.write(str(HIGH_SCORE))
            file.close()




    