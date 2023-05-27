from vpython import *
import time

#room with a marble
roof = box(pos=vector(0,-5,0), color=color.white, length=10, width=10, height=.1)
ground = box(pos=vector(0,5,0), color=color.green, length=10, width=10, height=.1)
left = box(pos=vector(-5,0,0), color=color.yellow, length=.1, width=10, height=10)
right = box(pos=vector(5,0,0), color=color.red, length=.1, width=10, height=10)
behind = box(pos=vector(0,0,-5), color=color.magenta, length=10, width=.1, height=10)
marble = sphere(pos=vector(0,0,0), color=color.blue, radius=1)

deltaX = .1
xPos = 0

while True:
    rate(60)
    xPos += deltaX
    if xPos > 3.95 or xPos < -3.95:
        deltaX *= -1
    marble.pos = vector(xPos,0,0)