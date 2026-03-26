import random

while True:
    #input from user
    print("Welcome to Password Generator")
    num_letters=int(input("Enter the number of letters: "))
    num_symbols=int(input("Enter number of symbols: "))
    num_numbers=int(input("Enter number of numbers: "))

    #parameters
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?' 
    numbers = '1234567890'

    #randomchoice
    password_chars = []

    password_chars += random.choices(letters, k=num_letters)
    password_chars += random.choices(symbols, k=num_symbols)
    password_chars += random.choices(numbers, k=num_numbers)

    random.shuffle(password_chars)

    password = ''.join(password_chars)

    print("Your password is:", password)

    z=input("Do you want to generate again? Y or N: ").lower()
    if(z!='y'):
        print("Thank You!")
        break
