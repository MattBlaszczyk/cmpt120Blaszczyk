# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 2/23/2018

# calculator.py
# A program that can calculate values when using the operations: +,-,/,*.

from graphics import *
from button import Button

class Calculator:

    # this class represents a GUI calculator

    def __init__(self):
        # Creating the window
        win = GraphWin("calculator")
        win.setCoords(0,0,6,7)
        win.setBackground("light green")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        # creating a grid of standard buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]
        self.buttons = []

        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, "="))
        # activation of buttons
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        answerBox = Rectangle(Point(.5,5.5), Point(5.5,6.5))
        answerBox.setFill('light blue')
        answerBox.draw(self.win)
        text = Text(Point(3,6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setSize(18)
        self.display = text

    def getButton(self):
        # returns the description of the button that was clicked on
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        # Refreshes the values displayed in the answer box
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            self.display.setText(text[:-1])
        elif key == '=':
            # finds errors in the text
            try:
                result = eval(text)
            except:
                result = 'Try Again'
            self.display.setText(str(result))
        else:
            self.display.setText(text+key)

    def run(self):
        # use of an infinite loop
        while True:
            key = self.getButton()
            self.processButton(key)

# runs the program
if __name__ == '__main__':
    theCalc = Calculator()
    theCalc.run()
    
