import random

def generate_prefix():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "@!#$?=+_-*%"
    prefix = random.choice(letters) + random.choice(letters) + random.choice(numbers) + random.choice(symbols)
    return prefix

def encrypt(text):
    key = {
        "a": "x", "b": "x", "c": "x",  
        "d": "1", "e": "1", "f": "1",  
        "g": "F", "h": "F", "i": "F",
        "j": "3", "k": "3", "l": "3",
        "m": "Y", "n": "Y", "o": "Y",
        "p": "i", "q": "i", "r": "i", "s": "i",
        "t": "#", "u": "#", "v": "#",
        "w": "9", "x": "9", "y": "9", "z": "9"
    }
    result = ""
    for letter in text.lower():
        if letter in key:
            result += key[letter]
        else:
            result += letter
    prefix = generate_prefix()
    return prefix + result

while True:
    text = input("Enter text to encrypt: ")
    print(encrypt(text))
    while True:
        password2 = input("Do you want another password encrypted? (yes/no) ").strip().lower()
        if password2 == "no":
            print("Thank you for using this password encrypter.")
            break
        elif password2 == "yes":
            break  
        else:
            print("Invalid input, please type yes or no!")
    if password2 == "no":
        break