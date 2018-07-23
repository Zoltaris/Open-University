# TM112 18D TMA02 Question 5

def float_rounded_up(float):
    """Round up a float to the nearest integer"""
    integer = int(float)
    if int(float) != float: 
        integer = int(float + 1)
    return integer


# Add your code here


"""This code calculates the volume of the floor. lFloor is the length,
wFloor is the width, and hFloor is the height, vFloor is the floor."""    
lFloor = 100
wFloor = 100
hFloor = 3
vFloor = lFloor * wFloor * hFloor

"""This code calculates the volume of the lorry cylinder
lCylinder is the length, rCylinder is the radius, vCylinder is the volume."""
lCylinder = 10
rCylinder = 3
vCylinder = rCylinder * rCylinder * lCylinder * 3.14159

"""This code calculates the number of cylinders needed."""

nCylinder = vFloor / vCylinder

""" This code calls the float_rounded_up function, in order to round up
the value calculated above, and assigns the rounded up value to a variable"""
nCylinderRounded = float_rounded_up(nCylinder)

"""This prints the above variable of the now rounded solution"""
print(nCylinderRounded)
