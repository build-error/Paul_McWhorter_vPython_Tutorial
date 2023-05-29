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

xlen = 20
ylen = 10
zlen = 7
thickness = .1

walls = [((xlen, thickness, zlen), (0, -ylen/2, 0), (0, ylen/2, 0)), ((thickness, ylen, zlen), (-xlen/2, 0, 0), (xlen/2, 0, 0)), ((xlen, ylen, thickness), (0,0,-zlen/2), (0,0,zlen/2))]

for i in [0,1,2]:
    for j in [1,2]:
        print(walls[i][0][0],walls[i][0][1],walls[i][0][2])
        print(walls[i][j][0], walls[i][j][1], walls[i][j][2])

        if (i, j) == (2, 2):
            continue

        boxTemp = box(size=vector(walls[i][0][0],walls[i][0][1],walls[i][0][2]), pos=vector(walls[i][j][0], walls[i][j][1], walls[i][j][2]), color=vector(random.randrange(0, 10)/10, random.randrange(0, 10)/10, random.randrange(0, 10)/10))

# while True:
#     pass

ballRadius = 1

marble = sphere(pos=vector(0,0,0), color=color.blue, radius=ballRadius)

deltaX = .1
xPos = 0

while True:
    rate(60)
    xPos += deltaX
    if abs(xPos) >  xlen/2 - thickness - ballRadius:
        deltaX *= -1
    marble.pos = vector(xPos,0,0)