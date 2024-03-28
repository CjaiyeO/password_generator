import random
import string
lengt=int(input("How many characters do you want your password to be ?\n=> "))

pu=input("Would you like to have special characters in your password ?\n=>")
di=input("Would you like to have numbers in your password ?\n=>")
punc = pu.lower() in ['yes', 'yeah','sure']
dig = di.lower() in ['yes', 'yeah','sure']


def generate_password(length=lengt):
    if(punc==True and dig==True):
        characters = string.ascii_letters + string.digits + string.punctuation
    if(punc==True and dig==False):
        characters = string.ascii_letters +  string.punctuation
    if(punc==False and dig==True):
        characters = string.ascii_letters + string.digits
    if(punc==False and dig== False):
        characters=string.ascii_letters 
        

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage: generate a 12-character password
print("Random Password:", generate_password())