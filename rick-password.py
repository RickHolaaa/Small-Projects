# Create a password generator

# Librairies

import string
import numpy as np
from random import *
# Code

def random_password(length):
    '''
        Create a random password of len characters
        len>=8
    '''
    lower_letter = list(string.ascii_lowercase)
    upper_letter = list(string.ascii_uppercase)
    special_char = [':', "'", '+', '[', '\\', '@', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    password = ""
    for i in range(length):
        chartype = np.random.choice([1,2,3],p=[0.4,0.3,0.3])
        if(chartype==1):
            password+=lower_letter[randrange(len(lower_letter))]
        
        elif(chartype==2):
            password+=upper_letter[randrange(len(upper_letter))]
        
        else:
            password+=special_char[randrange(len(special_char))]
    
    return password

def generate():
    print("Launching...")
    print("By launching this program, you'll be able to create a safe random password")
    len = input("Choose a length up to 8 (included)")
    print(random_password(len))
    #password = random_password(len)
    #print("Your random password is : " + password)
    return 0

#Launching

generate()