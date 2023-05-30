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

        if (i, j) == (2, 2):
            continue

        boxTemp = box(size=vector(walls[i][0][0],walls[i][0][1],walls[i][0][2]), pos=vector(walls[i][j][0], walls[i][j][1], walls[i][j][2]), color=vector(random.randrange(0, 10)/10, random.randrange(0, 10)/10, random.randrange(0, 10)/10))

mRadius = 1

marble = sphere(pos=vector(0,0,0), color=color.blue, radius=mRadius)

deltaX = .1
deltaY = .1
deltaZ = .1

thresholdx = xlen/2 - thickness/2 - mRadius
thresholdy = ylen/2 - thickness/2 - mRadius
thresholdz = zlen/2 - thickness/2 - mRadius

xPos = random.uniform(-thresholdx, thresholdx)
yPos = random.uniform(-thresholdy, thresholdy)
zPos = random.uniform(-thresholdz, thresholdz)

# e = random.uniform(0, 1) # coefficient of restitution (for releastic physics)
e = 1 # perfect elastic collision

while True:
    rate(60)
    xPos += deltaX
    yPos += deltaY
    zPos += deltaZ
    
    if abs(xPos) >=  xlen/2 - thickness/2 - mRadius: deltaX *= -e
    if abs(yPos) >=  ylen/2 - thickness/2 - mRadius: deltaY *= -e
    if abs(zPos) >=  zlen/2 - thickness/2 - mRadius: deltaZ *= -e

    marble.pos = vector(xPos,yPos,zPos)