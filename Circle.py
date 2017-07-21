import math
r=float(input('Enter the radius of the circle:'))
def calcArea(r):
    return math.pi*r**2
def calCircum(r):
    return math.pi*2*r
area=calcArea(r)
circumference=calCircum(r)
print('Area of the circle is %.2f\n'%area,'Circumference of the circle is %.2f'%circumference)
