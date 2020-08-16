import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Advanced Pong Game by Mateusz Hyla | @HylaTech")
wn.tracer(0)


# ----------- All Classes Space ----------------

class Sprite(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.pen = turtle.Turtle()

    def render(self):
        self.pen.goto(self.x, self.y)
        self.pen.stamp()


# ----------- End of All Classes Space ---------


while True:
    wn.update()

