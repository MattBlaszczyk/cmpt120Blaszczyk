# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 1/29/2018

# rover.py
# A program to calculate how long it takes a photo from the Mars Curiosity Rover to reach NASA

def mars():
    miles = eval(input("Enter distance that Mars is from Earth (in miles):"))
    time = miles * (1/186000)
    print("It will take the picture", time, "seconds to reach NASA from the Mars Curiosity Rover")

mars()

