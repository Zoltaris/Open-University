#Draw Tree with a number of levels

import math
from turtle import *
a = 10 #number of levels

speed(10) # set turtle speed - 1 slow 10 fast
left(120) # Sets turtle to correct orientation for beginning of code
for level in range (a): # loop to state how many triangles to code will run for
    #Draw a single triangle
    for line in range (3):
        left(120)
        forward(10*(level+1))

    # This next code moves to the start of next triangle   
    penup() #Lifts the pen
    left(150)
    print(level)
    y=(5*(level+1))
    print(y)
    z=(10*(level+1))
    print(z)
    x=(z**2)-(y**2)
    print(x)
    h=math.sqrt(x)
    print(h)
    forward(h)
    right(150)
    pendown()
