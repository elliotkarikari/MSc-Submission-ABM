# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot
"""


import random
import matplotlib.pyplot
def distance_between(agents_row_a, agents_row_b):
     return((agents_row_a[0] - agents_row_b[0]**2) + (agents_row_a[1]-agents_row_b[1]**2))**0.5

num_of_iterations = 100
num_of_agents = 100

agents= [] # Define agents with open tuple


#Creating Agent Based Model  
for i in range (num_of_agents):
    agents.append ([random.randint(0,99),random.randint(0,99)])
print(agents)
#Move the agents
for j in range (num_of_iterations):
    for i in range (num_of_agents):
    
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
print(agents)      

distance = distance_between(agents[0], agents[1])
print(distance)

matplotlib.pyplot.ylim(0, 99) 
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() # y and x points are meant to show, only one plots on map
