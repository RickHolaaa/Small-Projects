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
    y = int(input("Which line ?"))
    x = int(input("Which column ?"))
    while(free(tab,x,y)!=1):
        print("Wrong ! Retry...")
        y = int(input("Which line ?"))
        x = int(input("Which column ?"))
    tab[y][x]=1

def win(tab):
    winstatus = True
    # Rows :
    for i in range(len(tab)):
        for j in range(len(tab[i])-1):
            if tab[i][j]!=tab[i][j+1]:
                winstatus = False
        if((winstatus==True)and(tab[i][i]==1)):
            return 1
        elif((winstatus==True)and(tab[i][i]==2)):
            return 2
        else:
            winstatus=True
    # Columns :
    for i in range(len(tab[0])):
        for j in range(len(tab[i])-1):
            if(tab[j][i]!=tab[j+1][i]):
                winstatus=False
        if((winstatus==True)and(tab[j][i]==1)):
            return 1
        elif((winstatus==True)and(tab[j][i]==2)):
            return 2
        else:
            winstatus=True
    # Diagonals UPLEFT to BOTTOMRIGHT :
    for i in range(len(tab)-1):
        if(tab[i][i]!=tab[i+1][i+1]):
            winstatus=False
    if((winstatus==True)and(tab[i][i]==1)):
        return 1
    elif((winstatus==True)and(tab[i][i]==2)):
        return 2
    else:
        winstatus=False
    # Diagonals BOTTOMLEFT to UPRIGHT :
    for i in range(len(tab)-1):
        if(tab[len(tab)-1-i][i]!=tab[len(tab)-i-2][i+1]):
            winstatus=False
    if((winstatus==True)and(tab[len(tab)-1-i][i]==1)):
        return 1
    elif((winstatus==True)and(tab[len(tab)-1-i][i]==2)):
        return 2
    tie = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if(tab[i][j]==0):
                tie=1
    if(tie==0):
        return 0
    else:
        return -1
                

def game():
    tab = init_tab()
    who = who_start()
    if(who==1):
        print("You start first !")
        print_tab(tab)
        player(tab)
        print_tab(tab)
        while(((win(tab)!=1)and(win(tab)!=2))and(win(tab)!=0)):
            computer(tab)
            print_tab(tab)
            player(tab)
            print_tab(tab)
        if(win(tab)==1):
            print_tab(tab)
            print("You win !")
        elif(win(tab)==2):
            print_tab(tab)
            print("Computer wins !")
        else:
            print_tab(tab)
            print("It's a tie !")
    else:
        print("Computer starts first !")
        computer(tab)
        print_tab(tab)
        while(((win(tab)!=1)and(win(tab)!=2))and(win(tab)!=0)):
            player(tab)
            print_tab(tab)
            computer(tab)
            print_tab(tab)
        if(win(tab)==1):
            print_tab(tab)
            print("You win !")
        elif(win(tab)==2):
            print_tab(tab)
            print("Computer wins !")
        else:
            print_tab(tab)
            print("It's a tie !")


# Launching :
game()