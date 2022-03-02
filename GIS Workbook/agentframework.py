# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:58:58 2022

@author: Elliot
"""
#Import Library
import random

#Creating Agents
class Agent():
    def __init__ (self, i, environ, spy):#Agent Constructors
        self._x = random.randint(0,250)
        self._y = random.randint(0,250)
        self.env = environ
        self.store = 1
        self.agents = spy
        self.i = i
        print(self._y, self._x)
        
#function moving agents
    def move(self):#Move function 
    
        if random.random() < 0.5:
            self._y = (self._y + 1) % 250
        else:
            self._y = (self._y - 1) % 250

        if random.random() < 0.5:
            self._x = (self._x + 1) % 250
        else:
            self._x = (self._x - 1) % 250

#Agent eat whats left
    def eat(self): # Eat Function ..... can you make it eat what is left/can you make agents grow?
        
        if self.env[self._y][self._x] > 10:
            self.env[self._y][self._x] -= 10
            self.store += 10
       

#Defining Distance between agents            
    def distance_between(self, agent): 
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 
    
#Defining Shared Neighbourhood
    def shared_neigbourhood(self, neighbourhood):
    
        for agent in self.agents:
            distance = self.distance_between(agent)
            
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average

                print("sharing " + str(distance) + " " + str(average))

