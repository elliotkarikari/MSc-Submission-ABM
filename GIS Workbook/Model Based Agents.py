# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot
"""

#Model 1:
# Make a y variable.
from turtle import rt

y0 = 50
# Make a x variable.
x0 = 50

# Change y and x based on random numbers.
import random
random_number=random.random()

# Random walk one step
if random_number < 0.5:
     y0 = y0 + 1
     x0 = x0 + 1
else:
     y0 = y0 - 1
     x0 = x0 - 1 
     
print ("y0 =", y0, "x0 =", x0 , sep= (" "))

print()



#Model 2:
# Make a y variable.
y1 = 25
# Make a x variable.
x1 = 70

# Change y and x based on random numbers.

print ("y1 =", y1,  "x1 =", x1, sep= (" "))
# Make a second set of y and xs, and make these change randomly as well.
# Random walk one step
if random_number < 0.5:
     y1 = y1 + 1
     x1 = x1 + 1
else:
     y1 = y1 - 1
     x1 = x1 - 1 

# Work out the distance between the two sets of y and xs.

#√[(x2 – x1)2 + (y2 – y1)2].
# x0 = 0
# y0 = 0
# x1 = 3
# y1 = 4 #
dist = (((x1 - x0)**2) + ((y1 - y0)**2))** 0.5
print()

print("Pythagorian distance between y0, x0 and y1, x1  =", dist)


#Creating Agent Based Model 
agents= [] # Define agents with open tuple
agents.append ([random.randint(0,99),random.randint(0,99)])# randoms represent (y,x) 

NexAgent = agents + ([[random.randint(0,99),random.randint(0,99)]]) #Creating two separate tuples(Cordinate Systs)
print()
l = len(NexAgent)

for i in range(l -1):
    
    print(str(NexAgent[i] )+ ",")#Printing on separate lines
print(str(NexAgent[l -1] ))

import operator
print (max(NexAgent, key=operator.itemgetter(1)))

import matplotlib.pyplot

matplotlib.pyplot.ylim(0, 99) #Dont understand what this does in the code.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show() # y and x points are meant to show, only one plots on map
matplotlib.pyplot.scatter (agents[0][1],agents[0][0], color = 'green') # seek help on changing color toos

