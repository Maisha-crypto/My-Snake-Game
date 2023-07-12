from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# initialisation and setup of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='Snake')
screen.tracer(0)

# Creating an instance of class Snake
snake = Snake()
snake.create_snake()    # Creating the snake

# Creating an instance of the Food class
food = Food()

# Creating an instance of the Food class
score = Scoreboard()
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
    
    # detecting snake collision with food
    if snake.HEAD_OF_SNAKE.distance(food) <= 15:
        food.refresh_food()
        snake.grow_snake()
        score.clear()
        score.update_score()

    # detecting snake collision with wall
    if snake.HEAD_OF_SNAKE.xcor()>280 or snake.HEAD_OF_SNAKE.xcor()<-280 or snake.HEAD_OF_SNAKE.ycor()>280 or snake.HEAD_OF_SNAKE.ycor()<-280:
        isGameOn=False 
        score.game_over()

    # detect collision with tail
    for seg in snake.segments[1:]: # using slicing to eliminate the first segment when calsulating the distance

        if snake.HEAD_OF_SNAKE.distance(seg) < 10:
            isGameOn=False
            score.game_over()
             
screen.exitonclick()
