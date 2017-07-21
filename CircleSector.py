import math
r=float(input('Enter the radis of the circle: '))
x=float(input('The angle of a sector: '))
def calcArea(r,x):
    return (x/360)*2*math.pi*r**2
def calcCircum(r,x):
    return (x/360)*2*math.pi*r
area=  calcArea(r,x)
circum=calcCircum(r,x)
print('Area of a sector is %.2f \n'%area,'Length of a sector is %.2f'%circum)

