# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 4/27/2018
# tennismatch.py

from tennisplayer import Competitors

class TennisCompetition:
    def __init__(self, probA, probB):
        
        self.player1 = Competitors(probA)
        self.player2 = Competitors(probB)
        
        self.server = self.player1
        
        self.setsplayer1 = 0
        self.player1wins = 0
        
        self.setsplayer2 = 0
        self.player2wins = 0

    def switchServer(self):

        if self.server == self.player1:
            self.server = self.player2
        else:
            self.server = self.player1


    def game(self):
        
        while not self.end():
            if self.server.pointServe():
                self.server.addPoints()
            else:
                self.switchServer()
                self.server.addPoints()
                self.switchServer()

    
    def getScores(self):
        
        return self.player1.getPoints(), self.player2.getPoints()
    
    def set(self):
        
        x = self.Player1.getPoints()
        y = self.Player2.getPoints()
        
        if x > y + 10:
             self.setsplayer1 = self.setsplayer1 + 1
        else:
            self.setsplayer2 = self.setsplayer2 + 1

    def end(self):
        
        return self.player1.getPoints() == 50 or self.player2.getPoints() == 50 \
            or (self.player1.getPoints() == 40 and self.player2.getPoints() > 60) \
            or (self.player2.getPoints() > 60 and self.player1.getPoints() == 40)

            
    def GameOver(self):
        
        return self.sets == 3
    
    def Winner(self):
        
        while not GameOver():
            if self.setsplayer1 > self.setsplayer2:
                self.player1wins = self.player1wins + 1
            else:
                self.player2wins = self.player2wins + 1
