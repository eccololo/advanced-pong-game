import turtle
import random
import time
import math

WINDOW_WIDTH = 1600
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

    # FIXME:
    #   1. Here is something to fix.
    def is_collision(self, other):
        return math.sqrt(math.pow(self.x - other.x) + math.pow(self.y - other.y)) <= 0


class Player(Sprite):
    def __init__(self, x, y, color, shape, width, height):
        Sprite.__init__(self, x, y, color, shape, width, height)

    def move_down(self):
        self.y -= 30

    def move_up(self):
        self.y += 30


class Ball(Sprite):
    def __init__(self, x, y, color, shape):
        Sprite.__init__(self, x, y, color, shape, 1, 1)
        allowed_speeds = [-4, -3, -2, -1, 1, 2, 3, 4]
        rand_dx = random.choice(allowed_speeds)
        rand_dy = random.choice(allowed_speeds)
        self.dx = rand_dx
        self.dy = rand_dy

    def move(self):
        self.x -= self.dx
        self.y += self.dy

        if self._is_collision_border_top_y():
            self.dy *= -1
        elif self._is_collision_border_bottom_y():
            self.dy *= -1
        elif self._is_collision_border_left_x():
            self.dx *= -1
            self._reset_ball()
        elif self._is_collision_border_right_x():
            self.dx *= -1
            self._reset_ball()

    def _is_collision_border_top_y(self):
        return self.y > (WINDOW_HEIGHT / 2) - 10

    def _is_collision_border_bottom_y(self):
        return self.y < -((WINDOW_HEIGHT / 2) - 20)

    def _is_collision_border_left_x(self):
        return self.x < -((WINDOW_WIDTH / 2) + 10)

    def _is_collision_border_right_x(self):
        return self.x > (WINDOW_WIDTH / 2) - 10

    def _reset_ball(self):
        self.x = 0
        self.y = 0


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

