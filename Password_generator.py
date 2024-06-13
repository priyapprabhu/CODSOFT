''' A password generator is a useful tool that generates strong and random passwords for users. This
project aims to create a password generator application using python allowing users to specify the
length and complexity of the password.
User input: prompt the user to specify the desired length of the password. 
Generate password:use a combination of random characters to generate a password of specified length 
Display the password: print the generated password on the screen''' 

import random
import string

def generate_password(length):
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    digits= string.digits
    special_char= string.punctuation

    all_characters = lower + upper + digits + special_char

    password= ''. join(random.choice(all_characters) for i in range(length))
    return password

def main():
    length= int(input("Rnter the desired length of the password:"))
    password = generate_password(length)
    print("Generated Password:", password)

main()