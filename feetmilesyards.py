# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 1/23/2018

# convert.py
# A program to convert feet to miles to yards

def convert():
    feet = eval(input("Enter distance in feet:"))
    miles = 0.000189394 * feet
    yards = feet * 1/3
    print("The distance in miles is", miles , "miles.")
    print("The distance in yards is", yards , "yards.")
    
convert()
    
