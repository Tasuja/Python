number=[]
num=int(input("Enter a number:"))
a=0
while a<=num:
	number.append(a)
	a+=1
print(number)
print("The sum of all the natural numbers from 0 to %d are: %d"%(num,sum(number)))
