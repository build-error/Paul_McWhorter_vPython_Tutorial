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

walls = [((xlen, thickness, zlen), (0, -ylen/2, 0), (0, ylen/2, 0)), ((thickness, ylen, zlen), (-xlen/2, 0, 0), (xlen/2, 0, 0)), ((xlen, ylen, thickness), (0,0,-zlen/2), (0,0,zlen/2))]

for i in [0,1,2]:
    for j in [1,2]:
        print(walls[i][0][0],walls[i][0][1],walls[i][0][2])
        print(walls[i][j][0], walls[i][j][1], walls[i][j][2])
        boxTemp = box(size=vector(walls[i][0][0],walls[i][0][1],walls[i][0][2]), pos=vector(walls[i][j][0], walls[i][j][1], walls[i][j][2]), color=vector(random.randrange(0, 10)/10, random.randrange(0, 10)/10, random.randrange(0, 10)/10))

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