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

def animateLength(shape, delta, r, lower, upper, dir):
    if dir == 'up':
        while shape.length <= upper:
            rate(r)
            shape.length += delta

    elif dir == 'down':
        while shape.length > lower + delta:
            rate(r)
            shape.length -= delta

def animateOpacity(shape, delta, r, lower, upper, dir):
    if dir == 'up':
        while shape.opacity <= upper:
            rate(r)
            shape.opacity += delta

    elif dir == 'down':
        while shape.opacity > lower + delta:
            rate(r)
            shape.opacity -= delta

def animateRadius(shape, delta, r, lower, upper, dir):
    if dir == 'up':
        while shape.radius <= upper:
            rate(r)
            shape.radius += delta

    elif dir == 'down':
        while shape.radius > lower + delta:
            rate(r)
            shape.radius -= delta

if __name__ == '__main__':
    piston1 = cylinder(radius=1, length=0, color=color.red, opacity=1)
    delta = 0.01
    
    while True:
        animateLength(piston1, delta, 60, 0, 2, 'up')
        animateOpacity(piston1, delta, 60, 0, 1, 'down')
        animateOpacity(piston1, delta, 60, 0, 1, 'up')
        animateLength(piston1, delta, 60, 0, 2, 'down')
        animateLength(piston1, delta, 60, 0, 2, 'up')
        animateRadius(piston1, delta, 60, 0, 1, 'down')
        animateRadius(piston1, delta, 60, 0, 1, 'up')
        animateLength(piston1, delta, 60, 0, 2, 'down')