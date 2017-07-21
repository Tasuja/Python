import math
radius=float(input("Enter the radius of the circle: "))
def calcArea(radius):
	return math.pi*radius**2
def calcCircumference(radius):
	return 2*math.pi*radius
area=calcArea(radius)
circumference=calcCircumference(radius)
print ("Area of the circle is %.2f\n"%area,"\bCircumference of the circle is %.2f"%circumference)

	