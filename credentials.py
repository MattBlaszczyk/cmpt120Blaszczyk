# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Matt Blaszczyk
# Created: 2/23/2018


def firstName():
    first = input("Enter your first name: ")
    return(first)

def lastName():
    last = input("Enter your last name: ")
    return(last)

def username():
    for i in range(1):
        firstN=firstName();
        lastN=lastName();
        username = firstN + "." + lastN
        print("Your Marist username is: ", username)
        password = input("Create a new password: ")
        if len(password) >=8:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is",
                  username + "@marist.edu")
        elif len(password) <8:
            print("Fool of a Took! That password is feeble! Create a passwords with at least 8 charcters!")
            password = input("Create a new password: ")
            if len(password) >=8:
                print("The force is strong in this one…")
                print("Account configured. Your new email address is",
                  username + "@marist.edu")
username()

