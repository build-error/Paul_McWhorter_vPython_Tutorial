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

#ball changing colors
ball = sphere()
ball.color = color.red
time.sleep(1)
ball.color = color.green
time.sleep(1)
ball.color = color.blue

#ruler
myBox = box(color=color.yellow, length=12, width=1, height=0.2)

#tubes
myTube = cylinder(color=color.magenta, length=12, radius=1)
myTube = cylinder(color=color.magenta, length=12, width=1, height=.5)

#room with a marble
roof = box(pos=vector(0,-5,0), color=color.white, length=10, width=10, height=.1)
ground = box(pos=vector(0,5,0), color=color.green, length=10, width=10, height=.1)
left = box(pos=vector(-5,0,0), color=color.yellow, length=.1, width=10, height=10)
right = box(pos=vector(5,0,0), color=color.red, length=.1, width=10, height=10)
behind = box(pos=vector(0,0,-5), color=color.magenta, length=10, width=.1, height=10)
ball = sphere(pos=vector(0,0,0), color=color.blue, radius=1)
