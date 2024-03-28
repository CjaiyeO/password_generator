import random
import string
length=int(input("How many characters do you want your password to be ?\n=> "))       #asking user for size of password
punctuation=input("Would you like to have special characters in your password ?\n=>") #asking user 
digits=input("Would you like to have numbers in your password ?\n=>")                 #asking user 
punc = punctuation.lower() in ['yes', 'yeah','sure','yup','yessir']                   #for converting the input data to boolean value
dig = digits.lower() in ['yes', 'yeah','sure','yup','yessir']                         #for converting the input data to boolean value

#Actual function
def generate_password(length):                                                        
    if(punc==True and dig==True):                                                    
        characters = string.ascii_letters + string.digits + string.punctuation       #combination of letters, digits and special characters one character at a time
also he might want both in password or want neither in it 
    if(punc==True and dig==False):
        characters = string.ascii_letters +  string.punctuation                      #combination of letters and special characters. 
    if(punc==False and dig==True):
        characters = string.ascii_letters + string.digits                            #combination of letters and digits.
    if(punc==False and dig== False):
        characters=string.ascii_letters                                              #combination of letters only.
        

    password = ''.join(random.choice(characters) for i in range(length))             #for merging the randoms characters together.
    return password

print("Random Password:", generate_password(length))                                 #for printing the password. 
'''
let me explain the actual function here so basically there will be 4 scenarios 
or 4 types of passwords we can genrate with the help of this program

    let me explain with help of truth table
punctuation digits
0            0
0            1
1            0
1            1
    basically 0 means false 1 means true
so in 0 0 condition the password won contain any speacial characters as well as any digits
then in 0 1 no special characters but digits
then in 1 0 no digits but special charactes
finally in 1 1 both will be present
so according to users prefrence when this conditons will satisfy the block of code below this conditions will run and give desired output
 '''

