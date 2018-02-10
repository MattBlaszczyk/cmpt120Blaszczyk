# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 2/9/2018

# pi.py
# A program that approximates the value of pi and calculates the difference with the actual value

import math

def main():
    n = int(input("Enter number of terms to use:"))
    pi = 0
    sign = 1
    for i in range(1,n * 2 + 1, 2):
        term = (4/i*sign)
        pi = pi + term
        sign = sign * -1

    print("The approximate value of pi is:", pi)
    
    difference = (math.pi - pi)
    print("The difference between the value of pi and the approximate value of pi is:", difference)

main()
