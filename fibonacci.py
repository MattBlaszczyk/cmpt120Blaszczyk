# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 2/5/2018

# fibonacci.py
# A program that calculates the fibonacci number in the nth number of the sequence.


def fibonacci():
    x,y = 1,1
    
    nth = eval(input("Enter the desired sequence length:"))
    n=int(nth-2)
    
    for i in range(n):
        x,y=y,x+y
    print("A sequence length of", nth ,"gives you the fibonacci number of:", y)
    
fibonacci()
        
