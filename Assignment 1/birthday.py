import random
import matplotlib.pyplot as plt
import numpy as np
import math

def npr(n,r):
	return math.factorial(n)/math.factorial(n-r)
	
def direct_formula(group_size):
      return 100 - (npr(366,group_size)/math.pow(366,group_size))*100		#standard formula for Birthday paradox
      
def random_experiment(group_size):
	z = 0
	prob_value_list = list()
	while z < 100 :						#loop for average of different probablities found
		y = 0
		m = 0
		while m < 100 :					#100 set of random experiments to find percent probability
			n = 0
			birthday_list = list()
			while n < group_size :
				birthday_list.append(random.randrange(1,366))			#choose a random birthday
				n = n + 1
			birthday_set = set(birthday_list)
			if len(birthday_list) > len(birthday_set) :
				y = y + 1
			m = m + 1
		prob_value_list.append(y)
		z = z + 1
	return np.mean(prob_value_list)
      
ch='y'           
while ch=='y':            
	group_size = input("Enter the size of group : ")       
	print "Probability by Direct Formula:"
	print direct_formula(group_size)
	print "Probablity by Random Experiments:\n" + str(random_experiment(group_size))
	ch=raw_input("Continue? y/n : ")
	
x_axis=list()
y_axis1=list()
y_axis2=list()
for i in range(0,60):
	x_axis.append(i)
	y_axis1.append(direct_formula(i))
	y_axis2.append(random_experiment(i))

fig=plt.figure()

subplot1=fig.add_subplot(211)
subplot1.plot(np.array(x_axis),np.array(y_axis1))
plt.xlabel("Group size")
plt.ylabel("Percent probablity\n(Direct formula)")
plt.grid(True)

subplot2=fig.add_subplot(212)
subplot2.plot(np.array(x_axis),np.array(y_axis2))
plt.xlabel("Group size")
plt.ylabel("Percent probablity\n(Random Experiment)")
plt.grid(True)
plt.draw()
plt.show()	


	
	
