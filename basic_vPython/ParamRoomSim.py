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

xlen = 10
ylen = 10
zlen = 10
thickness = .1

walls = {(xlen, thickness, ylen):((0, -ylen/2, 0), (0, ylen/2, 0)), (thickness, ylen, zlen):((-xlen/2, 0, 0),(xlen/2, 0, 0)), (xlen, ylen, thickness):((0,0,-zlen/2),(0,0,zlen/2))}

for w in walls.keys():
    for i in range(2):
        boxTemp = box(size=vector(w[0],w[1],w[2]), pos=vector(walls[w][i][0], walls[w][i][1], walls[w][i][2]), color=vector(random.randrange(0, 10)/10, random.randrange(0, 10)/10, random.randrange(0, 10)/10))
    
while True:
    pass

# marble = sphere(pos=(0,0,0), color=color.blue, radius=1)

# deltaX = .1
# xPos = 0

# while True:
#     rate(60)
#     xPos += deltaX
#     if xPos > 3.95 or xPos < -3.95:
#         deltaX *= -1
#     marble.pos = (xPos,0,0)