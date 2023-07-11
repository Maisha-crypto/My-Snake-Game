from turtle import Turtle, Screen
import time
from snake import Snake

# initialisation and setup of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='Snake')
screen.tracer(0)

# Creating an instance of class Snake, and creating the snake
snake = Snake()
snake.create_snake()    
isGameOn = True

# initialisation of the screen listen functionality, and setup of the control functions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


while isGameOn:
    screen.update() # updating the screen once all the segments have moved
    time.sleep(0.1) # The delay between updates
    snake.move()    # Moving the snake
        
screen.exitonclick()
