# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot
"""

import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
     return(((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y-agents_row_b._y)**2))**0.5

num_of_iterations = 20
num_of_agents = 10

agents= [] # Define agents with open tuple


#Creating Agent Based Model  
for i in range (num_of_agents):
    agents.append (agentframework.Agent())

#Move the agents
for j in range (num_of_iterations):
    for i in range (num_of_agents):
        agents[i].move()
        
matplotlib.pyplot.ylim(0, 99) 
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show() # y and x points are meant to show, only one plots on map

for agents_row_a in agents:
    print("Distance Between Agents " +":")
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
    print(distance, end=" ")
    print()

a = agentframework.Agent()
print(a._y, a._x)
a.move()
print(a._y, a._x)

    