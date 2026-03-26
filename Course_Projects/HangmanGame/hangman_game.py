import random

# Hangman stages

stages = [
    '''
+---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''',
    '''
+---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

# Word list
words = ["APPLE", "MANGO", "STRAWBERRY", "PINEAPPLE", "WATERMELON"]

# Game function
def play_game():
    chosen_word = random.choice(words)
    lives = 5
    correct_guesses = []
    all_guesses = []

    placeholder = "_" * len(chosen_word)
    print("Word:", placeholder)

    game_over = False
    while not game_over:
        print("Lives =", lives)
        print(stages[lives])
        print("Guessed letters so far:", all_guesses)

        guess = input("Guess a letter: ").upper()

        if guess in all_guesses:
            print("You've already guessed that letter.")
            continue
        else:
            all_guesses.append(guess)

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print(stages[lives])
                print(f"**********************IT WAS {chosen_word} YOU LOSE**********************")
                game_over = True

        if guess in chosen_word and guess not in correct_guesses:
            correct_guesses.append(guess)

        display = ""
        for letter in chosen_word:
            if letter in correct_guesses:
                display += letter
            else:
                display += "_"
        print("Word:", display)

        if "_" not in display:
            print("********************************You Win********************************")
            game_over = True

# Run and ask to play again
while True:
    play_game()
    again = input("Play again? (Y/N): ").upper()
    if again != 'Y':
        print("Thank you for playing Hangman")
        break
