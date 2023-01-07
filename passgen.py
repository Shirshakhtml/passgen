import random
import string
import pyfiglet
import secrets

def banner(text):
    return pyfiglet.figlet_format(text)

print(banner('PASSGEN'))

def generate_password():
    length = int(input("Enter the desired password length: ")) # Ask the user for random password length
    characters = string.ascii_lowercase + string.digits + string.hexdigits + string.punctuation + string.ascii_uppercase + string.octdigits # Get a random assortment of numerals, uppercase letters, and lowercase letters
    password = ''.join(secrets.choice(characters) for i in range(length)) # In order to get a random password, mix up the characters
    return password

print(generate_password())
