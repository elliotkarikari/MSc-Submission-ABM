# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:13:15 2022

@author: Elliot

This exercise uses Object Oriented Programming to create an Agent Based Model 
(A model showing sheeps interaction with an environment)

Steps 

1. Import Libaries and files being worked with. (Line 29 - 38) 
The agentframe and environ files are integral parts of this 
model which allow it to run. Importing them here allows Model to read in code from these files. 

The matplotlib library allow us to visualise model (Line 118 - 125)

2. Create Agent - See Agentframework.py 

3. Function to find distance bewteen agents.
For function, distance_between, the program goes through rows x and y and calculates 
the distance using the Pythagoras' theorem.

4. Create Environment. - See environ.py 

5. Create Agent Based Model 
"""
# Imports Libraries 
import matplotlib
matplotlib.use('TkAgg') #TkAgg renders data to a tk Canvas
import tkinter 
import matplotlib.pyplot
import agentframework
import environ
import matplotlib.animation
import random
import requests
import bs4


#Defining Variables 
num_of_iterations = 500 # Number of times model runs 
num_of_agents = 20 # Agents in model 
neighbourhood = 20  # Neighbourhood Conversation


"""
WebScrapping 

Data from the site stated in the website below is drawn into this model
This data is assigned to x and y values determining its initial starting positon. 
"""

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


agents= [] # Creates List of Agents. 


""" Distance between all agents. This determines if agents are close enough to interact
Lines 70 - 71 setup the parameters for measuring distace. Lines 73 - 77 creates a loop
which goes through all agents runing the defined parameter."""

def distance_between(agents_row_a, agents_row_b):
     return(((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y-agents_row_b._y)**2))**0.5

for agents_row_a in agents:
    print("Distance Between Agents" + ":")
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance, end=" ")


#Reads in environment
environment = environ.readEnvironment()


#Define parameters of environment
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Environment Test - 
#a = agentframework.Agent(environment)
#print(a._y, a._x)


""" 
Agents are created and enabled to interact with its environment
The loop goes through the number of agents and 

"""  
for i in range (num_of_agents):  #Creats a loop going through number of agents 
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    
#Creates agents on line 103 and list while attaching the elements environment and agents.
    sheep = agentframework.Agent(i,environment, agents)
    agents.append(sheep)  
    
#Creates an extra agent to act as wolf
#wolf = agentframework.Agent(num_of_agents + 1,environ, agents)

"""



"""

def update(frame_number):
   
    fig.clear()   
    global carry_on
    

#Agentframework Tasks                                       
    random.shuffle(agents)    # Agent order is randomized 
    
#Loops through list of agents and calling agent methods    
    for i in range (num_of_agents):
        #print (agents[i].i)
        
        agent = agents[i]
        agent.move()
        agent.eat()
        agent.shared_neigbourhood(neighbourhood)
                  
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    else:
        carry_on = True
        #print("Continuing")

#Displays Agent onto Environment        
    matplotlib.pyplot.ylim(0,250) 
    matplotlib.pyplot.xlim(0,250)
    matplotlib.pyplot.imshow(environment)
    
    for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x,c="white") # y and x points are meant to show, only one plot on map

matplotlib.pyplot.show()
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
 
