# Introduction to Programming - Lab 8
# Author: Matt Blaszczyk
# Date: 4/13/2018
# ArtificialPersonality.py

from random import random

def main():
    print("Enter one of the following actions: reward, punish, threaten, joke.")
    ai = ["angry", "disgusted", "fearful", "happy", "sad", "suprised"]
    aiEmotionalState = int(random() * 6);
    C = [[1,0,4,3,3,3],[2,0,2,4,4,4],[0,1,2,4,4,2],[1,0,4,3,4,3]]
    
    def interaction():
        inter = input('I am ' + ai[aiEmotionalState] + ': ')
        if inter.lower() == "reward":
            return 0
        elif inter.lower() == "punish":
            return 1
        elif inter.lower() == "threaten":
            return 2
        elif inter.lower() == "joke":
            return 3
        else:
            return -1
        
    def searchEmotion(currEmotionalState, inputAction):
        return C[inputAction][currEmotionalState]

    while True:
        response = interaction()
        if response != -1:
            aiEmotionalState = searchEmotion(aiEmotionalState, response)
        else:
            print("This action is invalid")

main()

    
    









