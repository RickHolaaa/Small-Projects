# Rock Paper Scissor

# 1 Rock
# 2 Paper
# 3 Scissors

# Librairies :

import numpy as np

def computer():
    return np.random.randint(1,4)

def player():
    print(" 1 Rock \n 2 Paper \n 3 Scissors")
    play = input("Choose a number between 1 to 3 (included)")
    return play

def win(player, computer):
    if((player==1) and (computer==1)): #Rock vs Rock
        print("You choose rock and computer choose rock")
        return 0 # Draw
    elif ((player==1) and (computer==2)): #Rock vs Paper
        print("You choose rock and computer choose paper")
        return -1 # Loose
    elif ((player==1) and (computer==3)): #Rock vs Scissors
        print("You choose rock and computer choose scissors")
        return 1 # Win
    elif((player==2) and (computer==1)): #Paper vs Rock
        print("You choose paper and computer choose rock")
        return 1 # Win
    elif ((player==2) and (computer==2)): #Paper vs Paper
        print("You choose paper and computer choose paper")
        return 0 # Draw
    elif ((player==2) and (computer==3)): #Paper vs Scissors
        print("You choose paper and computer choose scissors")
        return -1 # Loose
    elif((player==3) and (computer==1)): #Scissors vs Rock
        print("You choose scissors and computer choose rock")
        return -1 # Loose
    elif ((player==3) and (computer==2)): #Scissors vs Paper
        print("You choose scissors and computer choose paper")
        return 1 # Win
    elif ((player==3) and (computer==3)): #Scissors vs Scissors
        print("You choose scissors and computer choose scissors")
        return 0 # Draw

def result(nb):
    if(nb==1):
        print("You're the winner !")
    elif(nb==0):
        print("It's a draw...")
    else:
        print("Sorry, you loose...")

def game():
    print("Welcome to the game Rock Paper Scissors")
    print("You'll play against a computer which will choose a random number between 1 to 3 (included)")
    comp = computer()
    agree = {1,2,3}
    play = player()
    while(play not in agree):
        play = player()
    res = win(play,comp)
    return result(res)

# Launching :

game()