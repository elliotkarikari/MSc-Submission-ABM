# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:58:58 2022

@author: Elliot
"""
#Import Library
import random

#Creating Agents - Defines what agent's characteristics 
class Agent():
    def __init__ (self, i, environ, spy):#Agent Constructors
        self._x = random.randint(0,250) # Constracts x randomly. Picks a random number from 0 - 250 for variable x
        self._y = random.randint(0,250) # Constracts y randomly. Picks a random number from 0 - 250 for variable y. This creates as many agents need for the model. 
        self.env = environ
        self.store = 1
        self.agents = spy
        self.i = i#position
        self.living = True
        #print(self._y, self._x)
        
                
#function moving agents
    def move(self):#Move function 
    
        random_generated = random.random()
        
        if random_generated < 0.2:
            self._y = (self._y + 1) % 250 #This provides parameters of movement for agents. It also creates a boundary (Torus) using the modulo sign %
        elif random_generated > 0.5:
            self._y = (self._y - 1) % 250
        else:
            pass
            

        if random.random() < 0.2:
            self._x = (self._x + 1) % 250
        elif random.random() > 0.5:
            self._x = (self._x - 1) % 250
        else:
            pass
        
        #print(random_generated) - Test - Generates random umber
        
    def get_store(self):
        return self.store
    
#Agent eat whats left
    def eat(self): # Eat Function ..... can you make it eat what is left/can you make agents grow?
        
        if self.env[self._x][self._y] > 10:                 #if x and y cordinates is greater than 10
            #print (self.env[self._x][self._y])
            self.env[self._x][self._y] -= 10                #take away 10
            self.store += 10                                #store 10
        else: 
            self.env[self._x][self._y] -= self.env[self._x][self._y]
            self.store += self.env[self._x][self._y]
       
        if self.store >= 150:
            #print("id ="+str(self.i) +"  Store =" +str(self.store))
            
            self.env[self._x][self._y] = self.store - 20
            self.store -=20
           #print("After giving:  "+str(self.store))
           
    def eatsheep(self, neighbourhood): # Eat Function ..... can you make it eat what is left/can you make agents grow?
    
        for agent_index,agent in enumerate(self.agents):
           #print("agent =", agent, "index =", agent_index, "agents", self.agents)
            distance = self.distance_between(agent)
            
            if distance <= neighbourhood:
                agent.living=False
        
             
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

                #print("sharing " + str(distance) + " " + str(average))
                





