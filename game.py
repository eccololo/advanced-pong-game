import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Advanced Pong Game by Mateusz Hyla | @HylaTech")
wn.tracer(0)


# ----------- All Classes Space ----------------

class Sprite(turtle.Turtle):
    def __init__(self, x, y, color, shape, size):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size
        self.pen = turtle.Turtle()

    def render(self):
        self.pen.goto(self.x, self.y)
        self.pen.color(self.color)
        self.pen.shape(self.shape)
        self.pen.pensize(self.size)
        self.pen.stamp()

    def update(self):
        pass

    def move_down(self):
        self.y -= 10

    def move_up(self):
        self.y += 10


# ----------- End of All Classes Space ---------

sprite = Sprite(100, 100, "red", "square", 20)

# ----------- Keyboard Binding Space -----------
wn.listen()
wn.onkeypress(sprite.move_down, "Down")
wn.onkeypress(sprite.move_up, "Up")

while True:
    wn.update()
    sprite.render()
