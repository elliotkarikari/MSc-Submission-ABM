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

The matplotlib library allow us to visualise model (Line 147 - 160)

2. Create Agents and Wolf- See Agentframework.py 

3. Function to find distance bewteen agents.
For function, distance_between, the program goes through rows x and y and calculates 
the distance using the Pythagoras' theorem.

4. Create Environment. - See environ.py 

5. Run Agent_Based_Model 
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
neighbourhood = 10  
agents= [] # Creates List of Agents.
wolves=[] # Creates List of wolves.


"""
WebScrapping 

Data from the site stated in the website below is drawn into this model
This data is assigned to x and y values determining its initial starting positon of Agents. 
"""

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

"""Web Scrapping test"""
print(td_ys, td_xs) 


#Reads in environment
environment = environ.readEnvironment()


"""Environment Test"""  
#a = agentframework.Agent(environment)
#print(a._y, a._x)


#Define parameters of Canvas
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


""" 
Agents are created and enabled to interact with its environment
The loop goes through the number of agents, determines its starting positions of agents and creates it by drawing out attributes 
from agentframework. It them appends it to the list forming agents

"""  
for i in range (num_of_agents):  #Creats a loop going through number of agents 
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    
#Creates agent instance on line 89 while attaching the elements environment and agents.
    sheep = agentframework.Agent(i,environment, agents, x, y)
    agents.append(sheep)  
        
""" 
Outside the loop we create a wolf which goes through the same motion of drowing out its attributes from the framework and 
creating a wolf

""" 
    
wolve= agentframework.Agent(num_of_agents, environment, agents, x, y)
wolves.append(wolve)


def update(frame_number):

    """Once canvas is drawn. It updates the canvas per frame_number. 
    
    If the arguement frame_number isn't passed frame is not updated.
    
    Parameters
    ----------
    frame_number : int,
        Number of times frames after which canvas is cleared and redrawn 
    ------
    """
    fig.clear()   
    global carry_on
    

#Agentframework Tasks                                       
    random.shuffle(agents)    # Agent order is randomized 
    
#Loops through list of agents and calls agent methods defined in agentframework. This gives agency to created agents   
    for i in range (num_of_agents):
        #print (agents[i].i)
        
        agent = agents[i]
#This if statement is a condition which states if agents are a live, show them on screen. If they die, take them off screen.
        if agent.living:
            agent.move()
            agent.eat()
            agent.shared_neigbourhood(neighbourhood)
#Wolves are outside the if statement because they are alive and doing the killing
        wolves[0].move()
        wolves[0].eatsheep(neighbourhood)
        
#what does this do ??????????????????????                    
    if random.random() < 0.1:
        carry_on = False
        #print("stopping condition")
    else:
        carry_on = True
        #print("Continuing")


#Displays Environment        
    matplotlib.pyplot.ylim(0,250) 
    matplotlib.pyplot.xlim(0,250)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlabel('Sheep are white, Wolf is brown')
    matplotlib.pyplot.title(label="Sheep in trouble, Wolf on the loose",
              loc="center",
              fontstyle='italic')
    
    
#Displays agents on Environment
    for i in range (num_of_agents):
        if agents[i].living:
            matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x,c="white") # y and x points (Sheep) plots on map, colour white
        matplotlib.pyplot.scatter(wolves[0]._y,wolves[0]._x,c="brown") # y and x points plot on map (wolf), colour brown


matplotlib.pyplot.show()

"""
Creates Graphic User Invterface. Run function and quit function are commands which all model to be run and stopped from GUI
tkinter.Menue creates the menu bar with model_menu.add_commands creating button to execute function defined above
"""

def run(): 
    
    """This runs simulation.  
    
    Parameters
    ----------
    Does not take any parameters.
    ------
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=50)
    canvas.draw()

def quit():
    
    """This stops the simulation.
    
    Parameters
    ----------
   Does not take any parameters. 
    ------
    """
    global root
    root.quit()

'''Creates GUI'''

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root,)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
                      
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 
model_menu.add_command(label="Clear model", command=quit, state="normal")


#tkinter.mainloop()



 
