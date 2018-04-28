# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 4/27/2018
# tennisplayer.py

from random import *

class Competitors:
    
    def __init__(self, prob):
        self.prob = prob
        self.points = 0

    def addPoints(self):
        if self.points == 0:
            self.points = self.points + 15
            
        elif self.points == 15:
            self.points = self.points + 15
            
        elif self.points == 30:
            self.points = self.points + 10
            
        elif self.points == 40:
            self.points = self.points + 10

     def pointServe(self):
        
        return random() <= self.prob

    def getPoints(self):
        
        return self.points
