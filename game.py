import turtle
import random
import math

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Advanced Pong Game by Mateusz Hyla | @HylaTech")
wn.tracer(0)
wn.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


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

    def update(self):
        self.pendown()
        self.pen.goto(self.x, self.y)
        self.pen.color(self.color)
        self.pen.shape(self.shape)
        self.pen.shapesize(self.width, self.height, None)
        self.pen.penup()

    def move_down(self):
        self.y -= 10

    def move_up(self):
        self.y += 10


class Player(Sprite):
    def __init__(self, x, y, color, shape, width, height):
        Sprite.__init__(self, x, y, color, shape, width, height)


class Ball(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape, 1, 1)
        self.speed = 3

    def move(self):
        self.x -= self.speed
        self.y += self.speed

        if self._is_collision_border_y():
            print("Collision Y!")
        elif self._is_collision_border_x():
            print("Collision X!")

    def _is_collision_border_y(self):
        return self.y > (WINDOW_HEIGHT / 2) - 5 or self.y < -((WINDOW_HEIGHT / 2) + 5)

    def _is_collision_border_x(self):
        return self.x > (WINDOW_WIDTH / 2) - 5 or self.x < -((WINDOW_WIDTH / 2) + 5)


# ----------- End of All Classes Space ---------

protector = Player(-500, 0, "green", "square", 5, 1)
agressor = Player(500, 0, "red", "square", 5, 1)
ball = Ball(0, 0, "green", "circle")

# ----------- Keyboard Binding Space -----------
wn.listen()
wn.onkeypress(agressor.move_down, "Down")
wn.onkeypress(agressor.move_up, "Up")
wn.onkeypress(protector.move_down, "s")
wn.onkeypress(protector.move_up, "w")

while True:
    wn.update()
    protector.update()
    agressor.update()
    ball.update()
    ball.move()
