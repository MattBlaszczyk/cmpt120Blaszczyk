# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 4/27/2018
# tennissimulation.py

from simstats import SimStats
from tennismatch import TennisCompetition

def getValues():
    
    probA = float(input("Please enter the probability of Player 1: "))
    
    probB = float(input("Please enter the probability of Player 2: "))
    
    z = int(input("Please enter the number of games played: "))
    
    return probA, probB, z

def displayGreeting():
    
    print("Hello.  This is a simulation of a series of tennis games")
    
def main():
    
    statistics = SimStats()
    displayGreeting()
    probA, probB, z = getValues()
    
    for i in range(z):
        Dual = TennisCompetition(probA, probB)
        Dual.game()
        statistics.update(Dual)
        
    statistics.printReport()

main()
