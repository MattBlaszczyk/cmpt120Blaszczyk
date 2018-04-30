# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 4/13/2018

# CalcProject4.py
# A program that can calculate values.
# Has functioning buttons including memory and special operations and grouping characters with modularized code
# Prints the values of the buttons clicked to assure the user that the operation occurs
# trigonemetric functions produce answers in terms of radian
# For any scientific function, "x" must already be present on the screen for the operation
# to function properly
# For the x**y finction, enter y in the shell

# The two displays were created in which the bottom dispaly completes the arithmetic as the equation is elongated.  

# JA: If you follow sequence 3 from the project it gives an error

from graphics import *
from button import Button
import math

class Calculator:
    def __init__(self):
        win = GraphWin("calculator")
        win.setCoords(0,0,8,27)   
        win.setBackground("light green")
        self.win = win
        self.__createButtons()
        self.__createDisplayEq()
        self.__createMemBox()
        self.__createDisplayAn()
        self.memory = "0"
        
    def __createButtons(self):
        bSpecs = [(1,19.5,'M+'), (2.5,19.5,'MS'), (4,19.5,'MR'), (5.5,19.5,'M-'), (7,19.5,'MC'),
                  (1,17,'('), (2.5,17,')'), (4,17,'%'), (5.5,17,'**2'), (7,17,'**0.5'),
                  (1,14.5,'7'), (2.5,14.5,'8'), (4,14.5,'9'), (5.5,14.5,'<-'), (7,14.5,'1/x'),
                  (1,12,'4'), (2.5,12,'5'), (4,12,'6'), (5.5,12,'*'), (7,12,'/'),
                  (1,9.5,'1'), (2.5,9.5,'2'), (4,9.5,'3'), (5.5,9.5,'+'), (7,9.5,'-'),
                  (1,7,'SCI'), (2.5,7,'0'), (4,7,'C'), (5.5,7,'.')]
        self.buttons = []
        
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))
        self.buttons.append(Button(self.win,Point(7,7),1.5,2.5,"="))
        for b in self.buttons:  b.activate()

    def __createSciButtons(self):
        bSpecs = [(1,19.5,'M+'), (2.5,19.5,'MS'), (4,19.5,'MR'), (5.5,19.5,'M-'), (7,19.5,'MC'),
                  (1,17,'('), (2.5,17,')'), (4,17,'%'), (5.5,17,'**2'), (7,17,'**0.5'),
                  (1,14.5,'7'), (2.5,14.5,'8'), (4,14.5,'9'), (5.5,14.5,'<-'), (7,14.5,'1/x'),
                  (1,12,'4'), (2.5,12,'5'), (4,12,'6'), (5.5,12,'*'), (7,12,'/'),
                  (1,9.5,'1'), (2.5,9.5,'2'), (4,9.5,'3'), (5.5,9.5,'+'), (7,9.5,'-'),
                  (1,7,'SCI'), (2.5,7,'0'), (4,7,'C'), (5.5,7,'.'), (1,4.5,'sin'), (2.5,4.5,'cos'), (4,4.5,'tan'), (5.5,4.5,'asin'), (7,4.5,'acos'),
                    (1,2,'atan'), (2.5,2,'log'), (4,2,'ln'), (5.5,2,'10**x'), (7,2,'x**y')]
        self.buttons = []
        
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,2.5,label))
        self.buttons.append(Button(self.win,Point(7,7),1.5,2.5,"="))
        for b in self.buttons:  b.activate()
        
    def __createMemBox(self):
        bg = Rectangle(Point(0.5,24), Point(1.5,26.5))   
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(1,25.25), "")  
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.M = text
        self.eqflag = False
        
    def __createDisplayEq(self):
        bg = Rectangle(Point(.5,24), Point(7.5,26.5))
        bg.setFill('light Blue')
        bg.draw(self.win)
        text = Text(Point(4.5,25.25), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display = text
        

    def __createDisplayAn(self):
        bg = Rectangle(Point(.5,21.5), Point(7.5,24))
        bg.setFill('light Blue')
        bg.draw(self.win)
        text = Text(Point(4,22.75), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display2 = text
        
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
            self.display2.setText("")
            self.eqflag=True
            return
        elif key == '<-':
            self.display.setText(text[:-1])
            return
        elif key == '+':
            try:
                result = eval(text)
                self.display2.setText(str(result))
            except:
                self.display2.setText(str(text))
        elif key == '-':
            try:
                result = eval(text)
                self.display2.setText(str(result))
            except:
                self.display2.setText(str(text))
        elif key == '*':
            try:
                result = eval(text)
                self.display2.setText(str(result))
            except:
                self.display2.setText(str(text))
        elif key == '/':
            try:
                result = eval(text)
                self.display2.setText(str(result))
            except:
                self.display2.setText(str(text))
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = 'Ooops! Error'
            self.display2.setText(str(result))
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
        if key == 'SCI':
            self.__createSciButtons()
            self.display.setText(text[:-1])
        if key == 'sin':
            try:
                result = math.sin(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'cos':
            try:
                result = math.cos(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'tan':
            try:
                result = math.tan(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'asin':
            try:
                result = math.asin(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'acos':
            try:
                result = math.acos(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'atan':
            try:
                result = math.atan(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'log':
            try:
                result = math.log10(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'ln':
            try:
                result = math.log(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == '10**x':
            try:
                result = 10**(eval(text))
                self.display2.setText(str(result))
            except:
                result = 'Ooops! Error'
                self.display2.setText(str(result))
        elif key == 'x**y':
            y = eval(input('Please Enter a Value for y:'))
            result = (eval(text))**y
            self.display2.setText(str(result))
            
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)
            
if __name__ == '__main__':
    theCalc = Calculator()
    theCalc.run()
