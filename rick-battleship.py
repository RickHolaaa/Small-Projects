#Game : Battleship
'''
    A 10x10 array
    5 ship sizes : 2,3,3,5 and 6

'''

#Import librairies

import random

#Code

from venv import create


def create_array():
    return [[0 for i in range(10)] for j in range(10)]

def print_game(game):
    cpt=0
    cpt2=0
    for i in range(14):
        if(i==0):
            print('y',end='  ')
        elif(i==1):
            print('x',end='  ')
        elif(i>=2 and i<12):
            print(cpt2,end='  ')
            cpt2+=1
        else:
            print(' ',end='  ')

    print(' ')
    for i in range(39):
        print('_',end='')
    print(' ')
    print(' ')
    for i in game:
        print(cpt,end='  ')
        print('|',end='  ')
        for j in i:
            print(j,end='  ')
        print('|',end='  ')
        print(cpt,end='')
        cpt+=1
        print(' ')

    cpt2=0
    for i in range(39):
        print('_',end='')
    print(' ')
    print(' ')
    for i in range(14):
        if(i==0):
            print('y',end='  ')
        elif(i==1):
            print('x',end='  ')
        elif(i>=2 and i<12):
            print(cpt2,end='  ')
            cpt2+=1
        else:
            print(' ',end='  ')
    print(' ')
    print(' ')

def move_available(game,x,y,direction,ship):
    '''
    ship :
    1 = 2 cases
    2 = 3 cases
    3 = 3 cases
    4 = 5 cases
    5 = 6 cases

    direction :
    1 = up
    2 = bottom
    3 = left
    4 = right
    '''
    if direction==1:
        if ship==1:
            for i in range(y,y-2,-1):
                if(game[i][x]!=0):
                    return -1
        elif ship==2 or ship==3:
            for i in range(y,y-3,-1):
                if(game[i][x]!=0):
                    return -1
        elif ship==4:
            for i in range(y,y-5,-1):
                if(game[i][x]!=0):
                    return -1
        elif ship==5:
            for i in range(y,y-6,-1):
                if(game[i][x]!=0):
                    return -1
        if(x>=0 and x<=9):
            if ship==1:
                if(y<=0 or y>9):
                    return -1
                else:
                    return 1
            elif ship==2:
                if(y<=1 or y>9):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(y<=2 or y>9):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(y<=3 or y>9):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(y<=4 or y>9):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==2:
        if ship==1:
            for i in range(y,y+2):
                if(game[i][x]!=0):
                    return -1
        elif ship==2 or ship==3:
            for i in range(y,y+3):
                if(game[i][x]!=0):
                    return -1
        elif ship==4:
            for i in range(y,y+5):
                if(game[i][x]!=0):
                    return -1
        elif ship==5:
            for i in range(y,y+6):
                if(game[i][x]!=0):
                    return -1
        if(x>=0 and x<=9):
            if ship==1:
                if(y>=9 or y<0):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(y>=8 or y<0):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(y>=7 or y<0):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(y>=6 or y<0):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(y>=5 or y<0):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==3:
        if ship==1:
            for i in range(x,x-2,-1):
                if(game[y][i]!=0):
                    return -1
        elif ship==2 or ship==3:
            for i in range(x,x-3,-1):
                if(game[y][i]!=0):
                    return -1
        elif ship==4:
            for i in range(x,x-5,-1):
                if(game[y][i]!=0):
                    return -1
        elif ship==5:
            for i in range(x,x-6,-1):
                if(game[y][i]!=0):
                    return -1
        if(y>=0 and y<=9):
            if ship==1:
                if(x<=0 or x>9):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(x<=1 or x>9):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(x<=2 or x>9):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(x<=3 or x>9):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(x<=4 or x>9):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==4:
        if ship==1:
            for i in range(x,x+2):
                if(game[y][i]!=0):
                    return -1
        elif ship==2 or ship==3:
            for i in range(x,x+3):
                if(game[y][i]!=0):
                    return -1
        elif ship==4:
            for i in range(x,x+5):
                if(game[y][i]!=0):
                    return -1
        elif ship==5:
            for i in range(x,x+6):
                if(game[y][i]!=0):
                    return -1
        if(y>=0 and y<=9):
            if ship==1:
                if(x>=9 or x<0):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(x>=8 or x<0):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(x>=7 or x<0):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(x>=6 or x<0):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(x>=5 or x<0):
                    return -1
                else:
                    return 1
        else:
            return -1

def play(game,x,y,direction,ship):

    if(move_available(game,x,y,direction,ship)==1):
        if direction==1:
            if ship==1:
                for i in range(y,y-2,-1):
                    game[i][x]=ship
            elif ship==2 or ship==3:
                for i in range(y,y-3,-1):
                    game[i][x]=ship
            elif ship==4:
                for i in range(y,y-5,-1):
                    game[i][x]=ship
            elif ship==5:
                for i in range(y,y-6,-1):
                    game[i][x]=ship
        elif direction==2:
            if ship==1:
                for i in range(y,y+2):
                    game[i][x]=ship
            elif ship==2 or ship==3:
                for i in range(y,y+3):
                    game[i][x]=ship
            elif ship==4:
                for i in range(y,y+5):
                    game[i][x]=ship
            elif ship==5:
                for i in range(y,y+6):
                    game[i][x]=ship
        elif direction==4:
            if ship==1:
                for i in range(x,x+2):
                    game[y][i]=ship
            elif ship==2 or ship==3:
                for i in range(x,x+3):
                    game[y][i]=ship
            elif ship==4:
                for i in range(x,x+5):
                    game[y][i]=ship
            elif ship==5:
                for i in range(x,x+6):
                    game[y][i]=ship
        elif direction==3:
            if ship==1:
                for i in range(x,x-2,-1):
                    game[y][i]=ship
            elif ship==2 or ship==3:
                for i in range(x,x-3,-1):
                    game[y][i]=ship
            elif ship==4:
                for i in range(x,x-5,-1):
                    game[y][i]=ship
            elif ship==5:
                for i in range(x,x-6,-1):
                    game[y][i]=ship
    else:
        print("MOUVEMENT IMPOSSIBLE")
    return game

def fill_game():
    cpt = 0
    game = create_array()
    print_game(game)
    print("Please place your ships")
    while(cpt<=4):
        if cpt==0:
            print("The ship selected is the 2-cases ship")
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==1:
            print("The ship selected is the 3-cases ship")
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
            print("The ship selected is the 3-cases ship")
        elif cpt==2:
            print("The ship selected is the 3-cases ship")
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==3:
            print("The ship selected is the 5-cases ship")
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==4:
            print("The ship selected is the 6-cases ship")
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        if(move_available(game,x,y,dir,cpt+1)==1):
            game = play(game,x,y,dir,cpt+1)
            print_game(game)
            cpt+=1
        else:
            print("Please retry...")
        return game

def move_available_computer(game,x,y,direction,ship):
    '''
    ship :
    1 = 2 cases
    2 = 3 cases
    3 = 3 cases
    4 = 5 cases
    5 = 6 cases

    direction :
    1 = up
    2 = bottom
    3 = left
    4 = right
    '''
    if direction==1:
        if(x>=0 and x<=9):
            if ship==1:
                if(y<=0 or y>9):
                    return -1
                else:
                    return 1
            elif ship==2:
                if(y<=1 or y>9):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(y<=2 or y>9):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(y<=3 or y>9):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(y<=4 or y>9):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==2:
        if(x>=0 and x<=9):
            if ship==1:
                if(y>=9 or y<0):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(y>=8 or y<0):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(y>=7 or y<0):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(y>=6 or y<0):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(y>=5 or y<0):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==3:
        if(y>=0 and y<=9):
            if ship==1:
                if(x<=0 or x>9):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(x<=1 or x>9):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(x<=2 or x>9):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(x<=3 or x>9):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(x<=4 or x>9):
                    return -1
                else:
                    return 1
        else:
            return -1
    elif direction==4:
        if(y>=0 and y<=9):
            if ship==1:
                if(x>=9 or x<0):
                    return -1
                else:        
                    return 1
            elif ship==2:
                if(x>=8 or x<0):
                    return -1
                else:
                    return 1
            elif ship==3:
                if(x>=7 or x<0):
                    return -1
                else:
                    return 1
            elif ship==4:
                if(x>=6 or x<0):
                    return -1
                else:
                    return 1
            elif ship==5:
                if(x>=5 or x<0):
                    return -1
                else:
                    return 1
        else:
            return -1

def fill_computer():
    game = create_array()
    cpt = 0
    while(cpt<=4):
        if cpt==0:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dir = random.randint(1,4)
        elif cpt==1:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dir = random.randint(1,4)
        elif cpt==2:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dir = random.randint(1,4)
        elif cpt==3:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dir = random.randint(1,4)
        elif cpt==4:
            x = random.randint(0,9)
            y = random.randint(0,9)
            dir = random.randint(1,4)
        if(move_available_computer(game,x,y,dir,cpt+1)==1):
            game = play(game,x,y,dir,cpt+1)
            cpt+=1
    return game
#Run
'''
game = create_array()
#game[6][3]=1
print_game(game)
print(move_available(game,1,1,1,1))

game=play(game,5,5,4,2)
game=play(game,5,1,2,4)
print_game(game)
'''
#fill_game()
print_game(fill_computer())
'''
game = create_array()
print(move_available(game,0,0,4,1))
game = play(game,0,0,4,1)
print_game(game)
'''