# Introduction to Programming
# Author: Matt Blaszczyk
# Date: 3/30/2018
# TicTacToe.py

def TicTacToe():
    print("Welcome to TicTacToe")
    print("Directions: Type the number corresponding to the position you would like to choose.")
    print("Have Fun!!!!!")
    print("")
    board = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6))

    def printBoard():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def player1():
        x = getPlayerMove()
        if board[x] == "X" or board[x] == "O":
            print("Spot is taken. Try again")
            player1()
        else:
            board[x] = "X"

    def player2():
        o = getPlayerMove()
        if board[o] == "X" or board[o] == "O":
            print("Spot is taken. Try again")
            player2()
        else:
            board[o] = "O"

    def getPlayerMove():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("Not Possible! Try again")
                        continue
                except ValueError:
                   print("Not Possible!. Try again")
                   continue

    def combo_check():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins! Congrats!")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins! Congrats!")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Tie Game!")
                return True

    while not end:
        printBoard()
        end = combo_check()
        if end == True:
            break
        print("Player 1. Choose your position")
        player1()
        print()
        printBoard()
        end = combo_check()
        if end == True:
            break
        print("Player 2. Choose your postion")
        player2()
        print()

    if input("Play again (y/n)") == "y":
        print()
        TicTacToe()

TicTacToe()
