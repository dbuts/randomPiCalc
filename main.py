from math import *
from random import randint

def calcPi():
	factor = 0
	prime = 0
	N = 1000
	def cofactor(x,y):
		if x%2 == 0 and y%2 ==0:
			return True
		if x > y:
			z = x
		else:
			z = y
		for i in range (3, int(z/2), 2):
			if x%i == 0 and y%i == 0:
				return True
		return False
		
	for i in range(0,N):
		x = int(randint(1,10000))
		y = int(randint(1,10000))
		if cofactor(x,y):
			factor +=1
		else:
			prime +=1
	
	
	calc = sqrt(6/(prime/N))
	return calc

def averages():
	completion = 0
	sum = 0
	for i in range(100):
		sum += calcPi()
		completion+=1
		print (str(completion) + " % Done")
	avg = sum/100
	
	print("Actual Pi: " + str(pi))
	print("Average Calculated Pi: " + str(avg))
	print("Percent Error: " + str(abs(((avg - pi)/pi)*100)))

averages()