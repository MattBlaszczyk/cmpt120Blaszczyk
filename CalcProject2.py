# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 3/9/2018

# CalcProject2.py
# A program that can calculate values.
# Has functioning buttons including memory and special operations with modularized code
# Could not figure out how to eliminate eval from the code
# Prints the values of the buttons clicked to assure the user that the operation occurs

from graphics import *
from button import Button
import math

class Calculator:
    def __init__(self):
        win = GraphWin("calculator")
        win.setCoords(0,0,8,13.5)   
        win.setBackground("light green")
        self.win = win
        self.__createButtons()
        self.__createDisplay()
        self.__createMemBox()
        self.memory = "0"
        
    def __createButtons(self):
        bSpecs = [(2.5,1,'0'), (4,1,'.'), (1,2.5,'1'), (2.5,2.5,'2'), (4,2.5,'3'),
                   (5.5,2.5,'+'), (7,2.5,'-'), (1,4,'4'), (2.5,4,'5'), (4,4,'6'),
                   (5.5,4,'*'), (7,4,'/'), (1,5.5,'7'), (2.5,5.5,'8'), (4,5.5,'9'),
                   (5.5,5.5,'<-'),(7,5.5,'C'), (2.5,7,'%'), (4,7,'**2'),(5.5,7,'**0.5'), (7,7,'1/x'),
                   (1,8.5,'M+'), (2.5,8.5,'MS'),(4,8.5,'MR'),(1,7,''), (5.5,8.5,'M-'),
                   (7,8.5,'MC')]
        self.buttons = []
        
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,1.25,label))
        self.buttons.append(Button(self.win,Point(6.25,1),3,1.25,"="))
        for b in self.buttons:  b.activate()
        
    def __createMemBox(self):
        bg = Rectangle(Point(0.5,11.5), Point(1.5,13))   
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(1,12.25), "")  
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.M = text
        self.eqflag = False
        
    def __createDisplay(self):
        bg = Rectangle(Point(.5,11.5), Point(7.5,13))
        bg.setFill('light Blue')
        bg.draw(self.win)
        text = Text(Point(4.5,12.25), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display = text
        
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
                
    def processButton(self, key):
        text = self.display.getText()
        innumber=text and text[-1].isdigit()
        result = 0
        print (key)
        if key == 'C':
            self.display.setText("")
            self.eqflag=True
            return
        elif key == '<-':
            self.display.setText(text[:-1])
            return
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = 'Ooops! Error'
            self.display.setText(str(result))
            print ('Result',result)
            self.eqflag=True
            return
        if key == 'MR':
            if not innumber:
                self.display.setText(text+self.memory)
            else: self.display.setText(self.memory)
        elif key == 'MC':
            self.memory = "0"
            self.M.setText('')
        elif key == 'MS':
            self.memory = text or '0'
            if self.memory != '0':
                self.M.setText('M')
        elif key == 'M+':
            self.memory = str(eval(text+'+'+str(self.memory)))
            if self.memory != '0':
                self.M.setText('M')
        elif key == 'M-':
            self.memory = str(eval(text+'-'+str(self.memory)))
            if self.memory != '0':
                self.M.setText('M')
        elif key == '1/x':
            try:
                result = 1/(int(text))
            except:
                result = 'Ooops! Error'
            self.display.setText(str(result))
        elif key == 'x**2':
            result = int(text)**2
            self.display.setText(str(result))
        else:
            if not self.eqflag or not key.isdigit():
                self.display.setText(text+key)
            else:
                self.display.setText(key)
            self.eqflag=False
            
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)
            
if __name__ == '__main__':
    theCalc = Calculator()
    theCalc.run()
