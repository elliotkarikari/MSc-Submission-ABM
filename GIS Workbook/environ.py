# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 17:41:21 2022

@author: Elliot
"""

"""
CSV containing details of raster grid is imported and read into model
It goes through data rows and appends it to our environment list. 
Thus creating our environment
""" 

import csv

#Function creating Environment
def readEnvironment(): #Define Funciton 
    environment = []    #
    with open('in.txt', newline='') as f: #Open and read text file with raster data
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
                #print(value)
            environment.append(rowlist)
           
    return environment

