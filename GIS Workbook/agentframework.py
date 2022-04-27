# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:58:58 2022

@author: Elliot
"""
#Import Library
import random



"""Class Agents - creates agent with defined characteristics
def move - gives agents capacity to move. Agents move one step at a time
def get store -   
def eat - enables agents to eat environment - Parameter if self.store >=150 allow agent to store excess eaten into environment
def eatsheep - enables wolf eat sheep 
def distance_between - finds distance between agents
def shared_neighbourhood - shares neighbourhood is distance between agents is less than neighbourhood
""" 
class Agent():
    def __init__ (self, i, environ, spy, x,y):#Agent Constructors
        """Agent Constructor.  
        
        If parameters aren't passes contrastor doesn't work. 
        
        Parameters
        ----------
        i: int 
        identity of agent
        
        environ: int
        environment
        
        spy: list 
        agent
        
        x: int 
        x position scrapped from website
        
        y: int 
        y position scrapped from website
        ------
        """    
        self._x = x # Constracts x randomly. Picks a random number from 0 - 250 for variable x
        self._y = y # Constracts y randomly. Picks a random number from 0 - 250 for variable y. This creates as many agents need for the model. 
        self.env = environ
        self.store = 1
        self.agents = spy
        self.i = i#position
        self.living = True
        #print(self._y, self._x) - Test if agents are being formed
        
                

    def move(self):#Move function function moving agents. When position is less than 0.2 move _y one step
        """This causes agents to move
        Self must be passed through function to enable movement 
        
        Parameters
        ----------
        self:            
        Its self.
        ------
        """
        random_generated = random.random()
        
        if random_generated < 0.2:
            self._y = (self._y + 1) % 250 #This provides parameters of movement for agents. It also creates a boundary (Torus) using the modulo sign %
        elif random_generated > 0.5:
            self._y = (self._y - 1) % 250
        else:
            pass
            
        if random.random() < 0.2: #When position is less than 0.2 move _x one step
            self._x = (self._x + 1) % 250
        elif random.random() > 0.5:
            self._x = (self._x - 1) % 250
        else:
            pass

        #print(random_generated) - Test - Generates random umber
        
    def get_store(self):
        return self.store
        """This shows store of agent. 
        Parameters
        ----------
        Self:
        Its self
        ------
        Return 
        ----------
        int
        """
    
#Agent eat whats left
    def eat(self): # Eat Function
        """This runs simulation.  
        
        An if statment is used. 
            Statement: if the position of x,y in environment is less than 10
            take 10 from environment and store 10
        
        Parameters
        ----------
        Does not take any parameters.
        ------
        """
        
        if self.env[self._x][self._y] > 10:                 #if x and y cordinates is greater than 10
            #print (self.env[self._x][self._y])
            self.env[self._x][self._y] -= 10                #take away 10
            self.store += 10                                #store 10
        else: 
            self.env[self._x][self._y] -= self.env[self._x][self._y]
            self.store += self.env[self._x][self._y]
       
        if self.store >= 150:
            #print("id ="+str(self.i) +"  Store =" +str(self.store))
            
            self.env[self._x][self._y] = self.store - 50
            self.store -=50
            #print("After giving:  "+str(self.store)) #Test - If excess is being stored in environment
           
    def eatsheep(self, neighbourhood): # Function that enables wolf eat sheep. 
        """This allows wolf to eat sheep.  
        
        Parameters
        ----------
        neighbourhood: list
        ------
        """
        for agent_index,agent in enumerate(self.agents):
           #print("index =", agent_index, "agents", self.agents)
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                agent.living=False
        
             
#Defining Distance between agents            
    def distance_between(self, agent): 
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 
        """This finds distacne between agents.  
        
        Parameters
        ----------
        agent: int
        ------
        """
#Defining Shared Neighbourhood
    def shared_neigbourhood(self, neighbourhood): #If distance between agents is less than neighbourhood agents share their store
        """This allows agent to share its neighbourhood
        
        Parameters
        ----------
        neighbourhood: int
        ------
        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average

                #print("sharing " + str(distance) + " " + str(average)) - Test if neighbourhood is being shared
                





