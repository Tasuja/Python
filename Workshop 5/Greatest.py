numbers=[]
while True:
	num=int(input('>'))
	if num==0: break
	numbers.append(num)
print(numbers)
print("Greatest number: %d"%(max(numbers)))
		