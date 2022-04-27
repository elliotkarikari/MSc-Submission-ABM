# elliotkarikari.github.io
# Portfolio
This project code located in the GIS Workbook folder uses __Agent Based Modelling__ to explore sheep behaviour in an environment. The agents are created and given its attributes in the __agentframework.py__ file. 

This is done by writing functions classes. Class Agents contains various functions def function which gives the created class Agents its attributes.     
The environment created in the __environ.py__ file by importing a CSV with rows of values. This is a raster file with pixel values. The __Model_Based_Agents.py__ file allows the agents to be read into the environment. Here we us __Object-Oriented Programming__ which allows multiple instruction to be run simulaneously. 

The model is run through __Model_Based_Agent.py__ file. 

The project contains runs a number of iterations: 500
Contins 2 major Agents: 
20 agents (Sheep) - They move, eat, store, share and store excess eaten into their environment.
& a wolf. 
The wolves - move (Chase sheep) and kill sheep when they are close enough. Dead sheep disapper from screen. 

The model is run through a GUI with a __Run Model__ button and can be stopped using the __Clear Model__ button 
