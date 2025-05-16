import pgzrun
from pgzero.actor import Actor

TITLE = "Arkanoid clon"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420


def draw():
    paddle.draw()
    #ball.draw()


def update():
    pass

pgzrun.go()