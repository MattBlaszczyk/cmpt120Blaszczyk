# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 1/29/2018

# evens.py
# A program to calculate even numbers between 2 and 20.

def evens():
    x = 0
    y = 2
    quantity = 10
    
    print("This program shows even numbers between 2 and 20.")
    
    for i in range(quantity):
        x = x + y
        print(x)

evens()
