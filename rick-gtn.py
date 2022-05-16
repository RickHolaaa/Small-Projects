#Guess the number

#Librairies
from math import *
from random import *

#Code

def printing():
    print("Launching...")
    print("Difficulty :")
    print("EASY : between 0 and 10 with 5 tries")
    print("INTERMEDIATE : between 0 and 100 with 7 tries")
    print("ADVANCED : between 0 and 1000 with 9 tries")
    print("EXPERT : between 0 and 100000 with 11 tries")
    number = input("Choose a number : 1-Beginner ; 2-Intermediate ; 3-Advanced ; 4-Expert")
    while((number<1)or(number>4)):
        number = input("Let's try again... Choose a number : 1-Beginner ; 2-Intermediate ; 3-Advanced ; 4-Expert")
    if(number==1):
        print("You choose the beginner level !")
    elif(number==2):
        print("You choose the intermediate level !")
    elif(number==3):
        print("You choose the advanced level !")
    else:
        print("You choose the expert level !")
    return number

def random_number(number):
    #Generate a random generator
    if(number==1):
        mystery = randrange(0,11,1)
    elif(number==2):
        mystery = randrange(0,101,1)
    elif(number==3):
        mystery = randrange(0,1001,1)
    else:
        mystery = randrange(0,100001,1)
    return mystery

def compare(number, mystery, cpt):
    if(number>mystery):
        print("Too high... Try lower")
        cpt-=1
        if(cpt==0):
            print("Sorry... You lose... The mystery number was " + str(mystery))
            return (-1,cpt)
        else:
            print(str(cpt) + " tries left")
            return (0,cpt)
    elif(number<mystery):
        print("Too low... Try higher")
        cpt-=1
        if(cpt==0):
            print("Sorry...You lose...The mystery number was " + str(mystery))
            return (-1,cpt)
        else:
            print(str(cpt) + " tries left")
            return (0,cpt)
    else:
        print("Congratulations ! You found the mystery number which was : " + str(mystery) + " tries remaining : " + str(cpt))
        return (1,cpt)

def inputnb(number):
    
    if(number==1):
        temp = input("Choose a number between 0 and 10 (included)")
        if((temp<0)or(temp>10)):
            return inputnb(number)
        else:
            return temp
    elif(number==2):
        temp = input("Choose a number between 0 and 100 (included)")
        if((temp<0)or(temp>100)):
            return inputnb(number)
        else:
            return temp
    elif(number==3):
        temp = input("Choose a number between 0 and 1000 (included)")
        if((temp<0)or(temp>100)):
            return inputnb(number)
        else:
            return temp
    else:
        temp = input("Choose a number between 0 and 100000 (included)")
        if((temp<0)or(temp>100000)):
            return inputnb(number)
        else:
            return temp        
    


def jeu():
    nb = printing()
    if(nb==1):
        cpt = 5
    elif(nb==2):
        cpt=7
    elif(nb==3):
        cpt=9
    else:
        cpt=11
    mystery = random_number(nb)
    temp = inputnb(nb)
    result,cpt = compare(temp,mystery,cpt)
    while((result!=-1)and(result!=1)):
        temp = inputnb(nb)
        result,cpt = compare(temp,mystery,cpt)
    return 0



# Testing

jeu()