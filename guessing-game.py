# CMPT 120 Intro to Programming
# Lab #5 – Conditional Execution and Strings
# Author: Matt Blaszczyk
# Created: 2/26/2018

# guessing-game.py
# A game which challenges the user to guess the correct animal

def main():
    animal = "octopus"
    print("Lets play a game!!")
    print("The program is thinking of an animal...")

    while True:
        name = input("Please guess the animal (If you wish to quit the game simply type, a word that starts with 'q'): ")
        firstchar = name[0]
        if name.lower() == "octopus":
            print("Congratulations! You are correct.")
            opinion = input("Do you like this type of animal? (y or n): ")
            if opinion == "y":
                print("Sweet, I like this animal too!")
            elif opinion == "n":
                print("Thats a shame.")
            break
        elif firstchar.lower() == "q":
            print("You have quit the game")
            break
        else:
            print("Incorrect, Try Again")
        
main()

    
