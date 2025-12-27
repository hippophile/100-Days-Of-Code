from turtle import Turtle

COLOR = "gold"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        
        
       
    def refresh_score(self, l_score, r_score):
        self.clear()
        self.ht()
        self.penup()
        self.goto(0, 330)
        self.color(COLOR)

    
        text = f"{l_score} : {r_score}"
        self.write(text, align="center", font=('Arial', 42, 'normal'))
    
