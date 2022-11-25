from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
TURNING_ANGLE = (0, 90, 180, 270)


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = []

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.pu()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)
        self.tail = self.segments[3:]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.__init__()

    def press_z(self):
        if self.head.heading() != TURNING_ANGLE[3]:
            self.head.setheading(TURNING_ANGLE[1])

    def press_q(self):
        if self.head.heading() != TURNING_ANGLE[0]:
            self.head.setheading(TURNING_ANGLE[2])

    def press_s(self):
        if self.head.heading() != TURNING_ANGLE[1]:
            self.head.setheading(TURNING_ANGLE[3])

    def press_d(self):
        if self.head.heading() != TURNING_ANGLE[2]:
            self.head.setheading(TURNING_ANGLE[0])
