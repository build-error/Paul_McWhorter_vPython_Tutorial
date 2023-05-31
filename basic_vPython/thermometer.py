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
import random
from myPiston import *

rod = cylinder(pos=vector(0, -2.5, 0), axis=vector(0, 5.1, 0), radius=.3, color=color.white, opacity=.3)

rodRed = cylinder(pos=vector(0, -2.5, 0), axis=vector(0, 0.0000001, 0), radius=.2, color=color.red)

bulb = sphere(pos=vector(0, -3, 0), radius=.8, color=color.white, opacity=.3)
bulbRed = sphere(pos=vector(0, -3, 0), radius=.7, color=color.red)

backboard = box(pos=vector(0, 0, -.3), height=7, width=.5, length=5, color=vector(139/255,69/255,19/255))

spacing = 1
tickPos = -2.5
while tickPos <= 2.5:
    box(length=.5, width=.1, height=.1, pos=vector(1, tickPos, 0), color=color.black)
    tickPos += spacing

spacing = 0.1
tickPos = -2.5
while tickPos <= 2.5:
    box(length=.25, width=.05, height=.05, pos=vector(1, tickPos, 0), color=color.black)
    tickPos += spacing

def animateTemp(shape, delta, r, currtemp, prevtemp, dir):
    if dir == 'up':
        animateLength(shape, delta, r, prevtemp/20, currtemp/20, dir)
    
    elif dir == 'down':
        animateLength(shape, delta, r, currtemp/20, prevtemp/20, dir)

prevtemp = 0
while True:
    currtemp = input('Enter temperature = ')

    if currtemp == 'q':
        exit(0)

    currtemp = float(currtemp)

    print(prevtemp, currtemp)

    if currtemp < prevtemp:
        animateTemp(rodRed, 0.05, 60, currtemp, prevtemp, 'down')

    elif currtemp > prevtemp:
        animateTemp(rodRed, 0.05, 60, currtemp, prevtemp, 'up')

    else:
        pass

    prevtemp = currtemp