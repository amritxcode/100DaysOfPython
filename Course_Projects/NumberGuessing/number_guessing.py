logo = r'''
   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\
'''
import random

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking about a number between 1 to 100.")
number = random.choice(list(range(1,101)))
print(number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#Easy Level 10 Attempts
game_over = False

if difficulty == 'easy':
        lives = 10
elif difficulty == 'hard':
        lives = 5
    
while not game_over:
        if lives == 0:
            print(f"You're out of attempts! The number was {number}.")
            game_over = True
            break
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_over = True
        elif abs(number - guess) >= 5 and guess > number:
            lives -= 1
            print("Too high")  
        elif abs(number - guess) >= 5 and guess < number:
            lives -= 1
            print("Too low")
        elif abs(number - guess) <= 5 and guess > number:
            lives -= 1
            print("High")
        elif abs(number - guess) <= 5 and guess < number:
            lives -= 1
            print("Low")