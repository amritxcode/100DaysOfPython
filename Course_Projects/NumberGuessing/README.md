# Number Guessing Game

This is a simple command-line based number guessing game built using Python. The game randomly selects a number between 1 and 100, and the player has to guess the correct number within a limited number of attempts.

## Game Rules

- The game will ask the player to select a difficulty level: `easy` or `hard`.
- Based on the selected difficulty:
  - **Easy**: The player gets 10 attempts to guess the number.
  - **Hard**: The player gets 5 attempts to guess the number.
- After each guess:
  - The game provides feedback whether the guess is "too high", "too low", or "high"/"low" (if the guess is close to the number).
  - The player's remaining attempts are displayed after each guess.
- If the player guesses the correct number, the game ends with a congratulatory message.
- If the player runs out of attempts, the game ends with the correct number being revealed.

## Features

- Random number generation between 1 and 100.
- Easy and Hard difficulty levels with a limited number of attempts.
- Feedback on whether the guess is too high, too low, or close to the number.
- User-friendly interface with a logo at the start.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/amritxcode/number_guessing.git
    ```

2. Navigate to the project directory.
    ```bash
    cd number_guessing
    ```

3. Run the game script.
    ```bash
    python number_guessing.py
    ```

4. Follow the prompts in the terminal to play the game.

## Example

Welcome to the number guessing game!
I'm thinking about a number between 1 to 100.
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low
You have 8 attempts remaining to guess the number.
Make a guess: 35
High
You have 7 attempts remaining to guess the number.
Make a guess: 30
You got it! The answer was 30.