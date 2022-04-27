# elliotkarikari.github.io
# Portfolio
This project code located in the GIS Workbook folder uses __Agent Based Modelling__ to explore sheep behaviour in an environment. The agents are created and given its attributes in the "agentframework.py" file. 

This is done by writing functions classes. Class Agents contains various functions __def__ function which give the created class Agents its attributes.     
The environment created in the "environ.py" file. This is a raster file with pixel values. The "Model_Based_Agents.py" file allows the agents to be read into the environment. Here we us __Object-Oriented Programming__ which allows multiple instruction to be run simulaneously. 

The model is run through "Model_Based_Agent.py" file. 

The project contains runs a number of iterations: 500
Contins 2 major Agents: 
20 agents (Sheep) - They move, eat, store, share and store excess eaten into their environment.
& a wolf. 
The wolves - move (Chase sheep) and kill sheep when they are close enough. Dead sheep disapper from screen. 

The model is run through a GUI with a __Run Model__ button and can be stopped using the __Clear Model__ button 
