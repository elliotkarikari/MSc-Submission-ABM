# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot
"""
#Import Libaries 
import matplotlib.pyplot
import agentframework
import environ
import matplotlib.animation


#Function to find distance bewteen agents 
def distance_between(agents_row_a, agents_row_b):
     return(((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y-agents_row_b._y)**2))**0.5

#Defining Number of agents 
num_of_iterations = 200
num_of_agents = 20
neighbourhood = 40

agents= [] # Define agents with open tuple

#Reading environment in Model Based Agent
environment = environ.readEnvironment()


#Creating Agent Based Model  
for i in range (num_of_agents):
    agents.append (agentframework.Agent(environment, agents))
   
#Agentframework Task
for j in range (num_of_iterations):
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].shared_neigbourhood(neighbourhood)

#Displays Agent onto Environment        
matplotlib.pyplot.ylim(0,250) 
matplotlib.pyplot.xlim(0,250)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x)
matplotlib.pyplot.show() # y and x points are meant to show, only one plots on map

#Finding Distance between agents
for agents_row_a in agents:
    print("Distance Between Agents" + ":")
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
    print(distance, end=" ")
    print()


#Environment Test
#a = agentframework.Agent(environment)
#print(a._y, a._x)
#a.move()
#print(a._y, a._x)

#Environment Test
#a = agents[7]._y
#b = agents[5]._x     
#print(a,b)
 
