# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot

The aim of this exercise is to create a model which interacts with an environment using Object Oriented Programming.

1. Import Libaries and files being worked with. (Line 25 - 29) 
The agentframe and environ files are integral parts of this 
model which allow it to run. Importing them here allows Model to read in code from these files. 

The matplotlib library allow us to visualise model (Line 73 - 78)

2. Create Agent - See Agentframework.py 

3. Function to find distance bewteen agents.(Line 42)
For function, distance_between, the program goes through rows x and y and calculates 
the distance using the Pythagoras' theorem.

4. Create Environment. - See environ.py 


"""

import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework
import environ
import matplotlib.animation
import random
 



#Defining Variables 
num_of_iterations = 500
num_of_agents = 10
neighbourhood = 20

# Define agents with open tuple
agents= [] 


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


def distance_between(agents_row_a, agents_row_b):
     return(((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y-agents_row_b._y)**2))**0.5

# Distance between all agents
for agents_row_a in agents:
    print("Distance Between Agents" + ":")
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance, end=" ")


#Reading environment in Model Based Agent
environment = environ.readEnvironment()

#Environment Test - 
#a = agentframework.Agent(environment)
#print(a._y, a._x)
#a.move()
#print(a._y, a._x)

	
#Creating Agent Based Model  
for i in range (num_of_agents):  #Creats a loop going through number of agents 
    agents.append (agentframework.Agent(i,environment, agents))     #Joins agentframworkmodel to agents list while attaching the elements environment and agents. 


carry_on = True

"""



"""

def update(frame_number):
    
    fig.clear()   
    global carry_on
#Agentframework Tasks                                       
    random.shuffle(agents)    # Agent order is randomized 
    for i in range (num_of_agents):
        #print (agents[i].i)
        agents[i].move()
        agents[i].eat()
        agents[i].shared_neigbourhood(neighbourhood)
            
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
        

#Displays Agent onto Environment        
    matplotlib.pyplot.ylim(0,250) 
    matplotlib.pyplot.xlim(0,250)
    matplotlib.pyplot.imshow(environment)
    for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x) # y and x points are meant to show, only one plots on map


"""

"""
def run():   
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=50)
    canvas.draw()

'''Creates GUI'''

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
                      
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 


tkinter.mainloop()




#Environment Test
#a = agents[7]._y
#b = agents[5]._x     
#print(a,b)
 
