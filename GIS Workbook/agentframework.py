# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:58:58 2022

@author: Elliot
"""
import random

class Agent():
    def __init__ (self):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        
        print(self._y, self._x)
        
    def move(self):
    
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

