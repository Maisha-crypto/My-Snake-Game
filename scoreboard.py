from turtle import Turtle

# Constants
ALIGNMENT = 'Center'
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!")

    def update_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        self.score+=1
