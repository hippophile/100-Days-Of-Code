from turtle import Turtle

COLOR = "gold"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        
    def refresh_score(self, score):
        self.clear()
        self.ht()
        self.penup()
        self.goto(0, 330)
        self.color(COLOR)

    
        text = f"Score is {score}"
        self.write(text, align="center", font=('Arial', 21, 'normal'))
    
    def game_over(self, score):
        # self.clear()
        self.ht()
        self.penup()
        self.color(COLOR)
        self.goto(2, -2)
        
        self.write("GAME OVER", align="center", font=('Courier', 30, 'bold'))
    
        self.goto(0, 0)
        self.color(COLOR)
        self.write("GAME OVER", align="center", font=('Courier', 30, 'bold'))

        self.goto(0, -40)
        self.color(COLOR)
        self.write(f"Final Score: {score}", align="center", font=('Arial', 18, 'normal'))
        