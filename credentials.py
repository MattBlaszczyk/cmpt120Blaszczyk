# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Matt Blaszczyk
# Created: 2/23/2018

def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first +"."+ last
    passwd = input("Create a new password: ")
    if len(passwd) >=8:
        print("The force is strong in this one…")
        print("Account configured. Your new email address is",
              uname + "@marist.edu")
    elif len(passwd) <8:
        print("Fool of a Took! That password is feeble! Create a passwords with at least 8 charcters!")
        passwd = input("Create a new password: ")
        if len(passwd) >=8:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is",
              uname + "@marist.edu")
main()
