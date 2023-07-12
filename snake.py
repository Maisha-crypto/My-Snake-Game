from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__ (self):
        '''This is a default constructor'''
        self.segments = []
        self.create_snake()
        self.HEAD_OF_SNAKE = self.segments[0]
        
    def create_snake(self):
        '''This method creates the initial snake, using 3 square segments.'''
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
            '''This function extends the snake when it collides with food'''
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def grow_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''This method moves the created segments one at a time '''
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.HEAD_OF_SNAKE.forward(MOVE_DISTANCE)
    
    def up(self):
        '''This method turns the first segment up, if the snake is no already going up.'''
        if self.HEAD_OF_SNAKE.heading() != DOWN:
            self.HEAD_OF_SNAKE.setheading(UP)

    def down(self):
        '''This method turns the first segment down, if the snake is not already going down.'''
        if self.HEAD_OF_SNAKE.heading() != UP:
            self.HEAD_OF_SNAKE.setheading(DOWN)

    def left(self):
        '''This method turns the first segment left, if the snake is not already going right.'''
        if self.HEAD_OF_SNAKE.heading() != RIGHT:
            self.HEAD_OF_SNAKE.setheading(LEFT)

    def right(self):
        '''This method turns the first segment right, if the snake is not already going left.'''
        if self.HEAD_OF_SNAKE.heading() != LEFT:
            self.HEAD_OF_SNAKE.setheading(RIGHT)

    