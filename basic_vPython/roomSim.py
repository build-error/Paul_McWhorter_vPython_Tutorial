#   vPython Orientation:
#     y
#     |
#     |  laptop
#     |  screen
#     |_ _ _ _ _ x 
#    /
#   / 
#  /  
# z (out of the screen)

from vpython import *
import time

#room with a marble
ground = box(pos=vector(0,-5,0), color=color.white, size=vector(10, .1, 10))
roof = box(pos=vector(0,5,0), color=color.green, size=vector(10, .1, 10))
left = box(pos=vector(-5,0,0), color=color.yellow, size=vector(.1, 10, 10))
right = box(pos=vector(5,0,0), color=color.red, size=vector(.1, 10, 10))
behind = box(pos=vector(0,0,-5), color=color.magenta, size=vector(10, 10, .1))
marble = sphere(pos=vector(0,0,0), color=color.blue, radius=1)

deltaX = .1
xPos = 0

while True:
    rate(60)
    xPos += deltaX
    if xPos > 3.95 or xPos < -3.95:
        deltaX *= -1
    marble.pos = vector(xPos,0,0)