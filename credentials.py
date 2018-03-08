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
        # JA: You should actually make the username lowercase
        username = username.lower()
        print("Your Marist username is: ", username.lower())
        password = input("Create a password: ")
        # JA: This you should move to it's own function
        if len(password) >=8 and password.isupper():
            print("The force is strong in this one…")
            print("Account configured. Your new email address is",
                username + "@marist.edu")
            quit()
        if password.islower() or len(password) <8:
            print("Fool of a Took! That password is feeble!Please add uppercase letters or have the password be at least 8 characters!")
            password = input("Try again, create a new password: ")
        if len(password) >=8:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is",
                username + "@marist.edu")
            quit()
        if password.islower() or len(password) <8:
                print("Failure to make password, restart program")
                quit()

username()

