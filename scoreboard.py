from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. Your Score is: {self.score}" , align="center", font=("Arial", 20, "bold"))