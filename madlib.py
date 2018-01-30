# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 1/30/2018

# madlib.py
# A program that produces a madlib when a user enters a series of words.

def madlib():

    adj = input("Enter an adjective:")
    animal = input("Enter a type of animal:")
    location = input("Enter a store name:")
    song = input("Enter a song name:")

    print("The", adj, animal, "wandered into", location, "and sang", song, ".")

madlib()
