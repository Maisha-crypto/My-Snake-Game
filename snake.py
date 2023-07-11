from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.HEAD_OF_SNAKE = self.segments[0]
        
    def create_snake(self):

        for position in STARTING_POSITION:
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.HEAD_OF_SNAKE.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.HEAD_OF_SNAKE.heading() != DOWN:
            self.HEAD_OF_SNAKE.setheading(UP)

    def down(self):
        if self.HEAD_OF_SNAKE.heading() != UP:
            self.HEAD_OF_SNAKE.setheading(DOWN)

    def left(self):
        if self.HEAD_OF_SNAKE.heading() != RIGHT:
            self.HEAD_OF_SNAKE.setheading(LEFT)

    def right(self):
        if self.HEAD_OF_SNAKE.heading() != LEFT:
            self.HEAD_OF_SNAKE.setheading(RIGHT)
