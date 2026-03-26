# Hangman Game

## Description
A simple text-based Hangman game in Python, where you try to guess a word by guessing letters one at a time. Each incorrect guess results in a part of a hangman being drawn, and you lose if the drawing is completed. If you guess the word before losing all lives, you win!

## Features
- Randomly selects a word from a list.
- Shows hangman stages based on the number of incorrect guesses.
- Tracks and displays the lives remaining.
- Prevents duplicate guesses.
- Displays the word with blanks or correctly guessed letters.
- Asks if you want to play again after the game ends.

## How to Play
1. The game will display blank spaces for each letter of the randomly chosen word.
2. You guess a letter one at a time.
3. If you guess correctly, the letter will replace the corresponding blank spaces.
4. If you guess incorrectly, a part of the hangman will be drawn, and you will lose one life.
5. The game ends when you either guess the word or lose all your lives.
6. You can play again after the game ends.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository or download the `hangman.py` file.
2. Open a terminal and navigate to the folder containing `hangman.py`.
3. Run the command:
   ```bash
   python hangman.py

## Example Output

Word: _ _ _ _ _

Lives = 5
+---+
  |   |
      |
      |
      |
      |
=========
Guess a letter: A
Word: A _ _ _ _
Lives = 5
+---+
  |   |
      |
      |
      |
      |
=========
Guess a letter: Z
Word: A _ _ _ _
Lives = 4
+---+
  |   |
  O   |
      |
      |
      |
=========
...

## Contributing

Feel free to fork the repository, submit issues, or create pull requests. If you'd like to contribute new words, improvements, or features, feel free to submit a pull request!
