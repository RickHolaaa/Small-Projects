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
            if j==-10:
                print('#',end='  ')
            elif j<0:
                print('X',end='  ')
            else:
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

def print_game2(game):
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
            if j==-10:
                print('#',end='  ')
            elif j<0:
                print('X',end='  ')
            else:
                print('0',end='  ')
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
            x = int(int(input("Enter the x coordinate")))
            y = int(int(input("Enter the y coordinate")))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==1:
            print("The ship selected is the 3-cases ship")
            x = int(int(input("Enter the x coordinate")))
            y = int(int(input("Enter the y coordinate")))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
            print("The ship selected is the 3-cases ship")
        elif cpt==2:
            print("The ship selected is the 3-cases ship")
            x = int(int(input("Enter the x coordinate")))
            y = int(int(input("Enter the y coordinate")))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==3:
            print("The ship selected is the 5-cases ship")
            x = int(int(input("Enter the x coordinate")))
            y = int(int(input("Enter the y coordinate")))
            dir = int(input("Enter the direction (U=1,B=2,L=3,R=4) use the number of the direction"))
        elif cpt==4:
            print("The ship selected is the 6-cases ship")
            x = int(int(input("Enter the x coordinate")))
            y = int(int(input("Enter the y coordinate")))
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

def count_game(game):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0
    for i in range(10):
        res1 += game[i].count(1)
        res2 += game[i].count(2)
        res3 += game[i].count(3)
        res4 += game[i].count(4)
        res5 += game[i].count(5)
    return (res1,res2,res3,res4,res5)

def fill2_computer():
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

def fill_computer():
    game = fill2_computer()
    while(count_game(game)!=(2,3,3,5,6)):
        game = fill2_computer()
    return game

def touch_ship(game,x,y,player):
    if player==1:
        if game[y][x]==0:
            print("Missed at (",x,",",y,") !")
            game[y][x]=-10
        elif game[y][x]==1:
            print("Touched at (",x,",",y,") !")
            game[y][x]=-1
        elif game[y][x]==2:
            print("Touched at (",x,",",y,") !")
            game[y][x]=-2
        elif game[y][x]==3:
            print("Touched at (",x,",",y,") !")
            game[y][x]=-3
        elif game[y][x]==4:
            print("Touched at (",x,",",y,") !")
            game[y][x]=-4
        elif game[y][x]==5:
            print("Touched at (",x,",",y,") !")
            game[y][x]=-5
        else:
            return (game,0)
        return (game,1)
    else:
        if game[y][x]==0:
            game[y][x]=-10
        elif game[y][x]==1:
            game[y][x]=-1
        elif game[y][x]==2:
            game[y][x]=-2
        elif game[y][x]==3:
            game[y][x]=-3
        elif game[y][x]==4:
            game[y][x]=-4
        elif game[y][x]==5:
            game[y][x]=-5
        else:
            return (game,0)
        return (game,1)        

def run_game():
    '''
    1 = Player
    0 = Computer
    '''
    start = random.randint(0,1)
    if start==1:
        print("You start !")
        game_player = fill_game()
        game_computer = fill_computer()
        x = int(input("Enter the x coordinate"))
        y = int(input("Enter the y coordinate"))
        game_computer,boole = touch_ship(game_computer,x,y,1)
        while(((x<0 or x>9) or (y<0 or y>9)) or boole==0):
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            game_computer,boole = touch_ship(game_computer,x,y,1)
        print_game2(game_computer)
        while(count_game(game_player)!=(0,0,0,0,0) and count_game(game_computer)!=(0,0,0,0,0)):
            x_comp = random.randint(0,9)
            y_comp = random.randint(0,9)
            game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
            while(((x_comp<0 or x_comp>9) or (y_comp<0 or y_comp>9)) or boole_comp==0):
                x_comp = random.randint(0,9)
                y_comp = random.randint(0,9)
                game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            game_computer,boole = touch_ship(game_computer,x,y,1)
            while(((x<0 or x>9) or (y<0 or y>9)) or boole==0):
                x = int(input("Enter the x coordinate"))
                y = int(input("Enter the y coordinate"))
                game_player,game_computer = touch_ship(game_computer,x,y,1)
            print_game2(game_computer)
    else:
        print("Computer starts !")
        game_player = fill_game()
        game_computer = fill_computer()
        x_comp = random.randint(0,9)
        y_comp = random.randint(0,9)
        game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
        while(((x_comp<0 or x_comp>9) or (y_comp<0 or y_comp>9)) or boole_comp==0):
            x_comp = random.randint(0,9)
            y_comp = random.randint(0,9)
            game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
        while(count_game(game_player)!=(0,0,0,0,0) and count_game(game_computer)!=(0,0,0,0,0)):
            x = int(input("Enter the x coordinate"))
            y = int(input("Enter the y coordinate"))
            game_computer,boole = touch_ship(game_computer,x,y,1)
            while(((x<0 or x>9) or (y<0 or y>9)) or boole==0):
                x = int(input("Enter the x coordinate"))
                y = int(input("Enter the y coordinate"))
                game_computer,boole = touch_ship(game_computer,x,y,1)
            print_game2(game_computer)
            x_comp = random.randint(0,9)
            y_comp = random.randint(0,9)
            game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
            while(((x_comp<0 or x_comp>9) or (y_comp<0 or y_comp>9)) or boole_comp==0):
                x_comp = random.randint(0,9)
                y_comp = random.randint(0,9)
                game_player,boole_comp = touch_ship(game_player,x_comp,y_comp,0)
    if(count_game(game_player)==(0,0,0,0,0)):
        print("You win !")
        print("Your plate : ")
        print_game2(game_player)
        print("Computer's plate : ")
        print_game2(game_computer)
    if(count_game(game_computer)==(0,0,0,0,0)):
        print("You lose !")
        print("Your plate : ")
        print_game2(game_player)
        print("Computer's plate : ")
        print_game2(game_computer)

#Run
'''
game = create_array()
#game[6][3]=1
print_game(game)
print(move_available(game,1,1,1,1))

game=play(game,5,5,4,2)
game=play(game,5,1,2,4)
game = touch_ship(game,5,5)
print_game(game)
'''

'''
game = create_array()
print(move_available(game,0,0,4,1))
game = play(game,0,0,4,1)
print_game2(game)
touch_ship(game,0,0)
touch_ship(game,1,0)
touch_ship(game,2,0)
print_game2(game)
'''

run_game()