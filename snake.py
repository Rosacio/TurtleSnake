from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class SnakeTurtle:
    def __init__(self):
        self.turtles = []
        self.create_SnakeTurtle()
        self.head = self.turtles[0]


    def create_SnakeTurtle(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
            for tur_num in range(len(self.turtles) - 1, 0, -1):
                new_x = self.turtles[tur_num - 1].xcor()
                new_y = self.turtles[tur_num - 1].ycor()
                new_heading = self.turtles[tur_num - 1].heading()
                self.turtles[tur_num].goto(new_x, new_y)
                self.turtles[tur_num].setheading(new_heading)
            self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def add_segment(self, position):
        new_turtle = Turtle("turtle")
        new_turtle.color("cyan")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for tur in self.turtles:
            tur.goto(1000, 1000)
        self.turtles.clear()
        self.create_SnakeTurtle()
        self.head = self.turtles[0]
        
            
