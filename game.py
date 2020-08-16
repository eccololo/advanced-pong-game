import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Advanced Pong Game by Mateusz Hyla | @HylaTech")
wn.tracer(0)


# ----------- All Classes Space ----------------

class Sprite(turtle.Turtle):
    def __init__(self, x, y, color, shape, width, height):
        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.width = width
        self.height = height
        self.pen = turtle.Turtle()
        self.dx = 10
        self.dy = 10
        self.max_dy = 40
        self.max_dx = 40
        self.min_dy = 10
        self.min_dx = 10

    def update(self):
        self.pendown()
        self.pen.goto(self.x, self.y)
        self.pen.color(self.color)
        self.pen.shape(self.shape)
        self.pen.shapesize(self.width, self.height, None)
        self.pen.penup()

    def move_down(self):
        self.dy += 1
        if self.dy <= self.max_dy:
            self.y -= self.dy

    def move_up(self):
        self.dy += 1
        if self.dy <= self.max_dy:
            self.y += self.dy

    def reset_move(self):
        self.dy = self.min_dy
        self.dx = self.min_dx


# ----------- End of All Classes Space ---------

sprite = Sprite(100, 100, "red", "square", 5, 1)

# ----------- Keyboard Binding Space -----------
wn.listen()
wn.onkeypress(sprite.move_down, "Down")
wn.onkeypress(sprite.move_up, "Up")

while True:
    wn.update()
    sprite.update()
