from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.move()

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
        self.segments[0].forward(20)