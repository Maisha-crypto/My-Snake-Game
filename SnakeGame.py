from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='Snake')
screen.tracer(0)

snake = Snake()
snake.create_snake()    
isGameOn = True

while isGameOn:
    screen.update()
    time.sleep(0.2)
    snake.move()
        
screen.exitonclick()
