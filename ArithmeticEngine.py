# Introduction to Programming - Lab 6
# Author: Matt Blaszczyk
# Date: 3/21/2018
# ArithmeticEngine.py

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")

    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        
        if cmd in ("sub", "add", "mult", "div"):
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: ")) 
        if cmd == "add":
            result = num1 + num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "sub":
            result = num1 - num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "mult":
            result = num1 * num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "div":
            result = num1 // num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "quit":
            break
        else:
            print(cmd, "is not a valid comment")
    
def main():
    showIntro()
    doLoop()
    showOutro()
main()

