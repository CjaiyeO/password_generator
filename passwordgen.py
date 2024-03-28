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
        characters = string.ascii_letters + string.digits + string.punctuation        
also he might want both in password or want neither in it 
    if(punc==True and dig==False):
        characters = string.ascii_letters +  string.punctuation
    if(punc==False and dig==True):
        characters = string.ascii_letters + string.digits
    if(punc==False and dig== False):
        characters=string.ascii_letters 
        

    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Random Password:", generate_password(length))
