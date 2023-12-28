# This is a game of Rock, Paper, Scissors

print("This is a game of rock paper scissors.")

import random

startchoice = int(input("Start(1) or quit(2)?")) #Take user input for the start.

def game(choice):   #The game skeleton.
    
    num = choice
    if num == 1: #Get the choices of the player.
        print("Awesome! Lets get started.")
        while num == 1:
            gamer = int(input("Please enter a number 0-2. 0 is Rock, 1 is Paper, 2 is Scissors. Lets see who wins!\n(To quit, enter 3.)"))
            if gamer == 3:
                return "You quit; hope it was fun!"
                break
            elif (gamer != 0) and (gamer != 1) and (gamer != 2) and (gamer != 3):
                return "Invalid input. Try again?"
            else:
                print(winner(computerchoice(),playerchoice(gamer)))
            
    elif num == 2:
        return "Awe man, maybe next time :/. The program has ended."


def computerchoice(): #Get the computer's choice.
    computerguess = random.randint(0,2)
    

    if computerguess == 0:
        print("The computer chose rock,")
    elif computerguess == 1:
        print("The computer chose Paper.")
    elif computerguess == 2:
        print("The computer chose scissors.")

    return computerguess

def playerchoice(choice): #Get the players choice.

    if choice == 0:
        print("The Player chose rock,")
    elif choice == 1:
        print("The Player chose Paper.")
    elif choice == 2:
        print("The Player chose scissors.")

    return choice

def winner(cpu,player): #Determine the winner based on all possible instances.
    
    if (cpu == 1) and (player == 0):
        return "Computer wins with paper!"
    elif (cpu == 0) and (player == 1):
        return "The player wins with paper!"
    elif (cpu == 0) and (player == 2):
        return "Computer wins with Rock!"
    elif (cpu == 2) and (player == 0):
        return "The player wins with rock!"
    elif (cpu == 2) and (player == 1):
        return "Computer wins with scissors!"
    elif (cpu == 1) and (player == 2):
        return "Player wins with scissors."
    elif cpu == player:
        return "Its a draw!"

#Implement the game!
game(startchoice)
