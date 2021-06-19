import random
import time
import gameFunctions
import professions
import gamePlay as gP


print("Welcome to my first game a text based adventure game")
name = input("What is your name? ")
wants_to_play = (input("Hi " + name + " do you want to play my game? \n"
                                           "Yes or No: "))
if wants_to_play == "Yes":
    print("Awesome let's play")
    gP.game_play()
else:
    print("That's alright thanks for stopping by")



