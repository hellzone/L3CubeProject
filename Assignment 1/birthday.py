import random
import numpy as np
import math

def npr(n,r):
	return math.factorial(n)/math.factorial(n-r)
            
            
t = input("Enter the size of group : ")       
print "Direct Formula"
print 100 - (npr(366,t)/math.pow(366,t))*100
print "Random Experiments"
z = 0
x = list()
while z < 100 :
	y = 0
	m = 0
	while m < 100 :
		n = 0
		l = list()
		while n < t :
			l.append(random.randrange(1,366))
			n = n + 1
		s = set(l)
		if len(l) > len(s) :
			y = y + 1
		m = m + 1
	x.append(y)
	z = z + 1
print np.mean(x)
