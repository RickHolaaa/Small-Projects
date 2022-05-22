# Tic-tac-toe

# X Player 1
# O Computer 2

# Librairies :
from __future__ import print_function
import numpy as np

# Code :

def init_tab():
    return [ [0 for i in range(3)] for j in range(3)]

def print_tab(tab):
    print("-------")
    for i in tab:
        print("|", end="")
        for j in i:
            if(j==1):
                print("O", end = "")
            elif(j==2):
                print("X", end = "")
            else:
                print(" ", end = "")
            print("|", end = "")
        print("\n")
    print("-------")

def who_start():
    # 0 = Computer
    # 1 = Player
    return np.random.choice(2,1,p=[0.5,0.5])[0]

def free(tab,x,y):
    if(tab[y][x]==0):
        return 1
    else:
        return 0
    
def computer(tab):
    x = np.random.randint(0,3)
    y = np.random.randint(0,3)
    while(free(tab,x,y)!=1):
        x = np.random.randint(0,3)
        y = np.random.randint(0,3)
    tab[y][x]=2

def player(tab):
    y = input("Which line ?")
    x = input("Which column ?")
    while(free(tab,x,y)!=1):
        print("Wrong ! Retry...")
        y = input("Which line ?")
        x = input("Which column ?")
    tab[y][x]=1

#def win(tab):


def game():
    who = who_start()
    if(who==1):
        print("You start first !")
    else:
        print("Computer starts first !")


# Launching :
tab = init_tab()
print_tab(tab)
print(who_start())