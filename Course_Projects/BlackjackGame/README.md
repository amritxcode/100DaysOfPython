# Blackjack Console Game in Python

## Overview

This is a simple **Blackjack** card game implemented in Python for the console.  
It allows a single player to play against the dealer (computer) following standard Blackjack rules.

The program deals cards to the player and the dealer, showing one of the dealer's cards face-up while hiding the other until the player finishes their turn.

---

## Features

- Player vs Dealer game play.
- Standard deck values: Aces (can be 11 or 1), face cards as 10.
- Dealer hits until their total is 17 or higher.
- Player can choose to hit (get another card) or stand (stop).
- Automatic handling of Ace values to prevent busting.
- Game results include player win, dealer win, bust, or tie.
- Simple text-based interface.

---

## How to Play

1. Run the Python script.
2. Enter your name when prompted.
3. You will receive two cards; your total will be displayed.
4. One dealer card is shown, the other remains hidden until you stand.
5. Type `Y` to hit (get another card) or `N` to stand.
6. The dealer will play after you stand.
7. The winner will be announced.

---

## Requirements

- Python 3.x
- No additional libraries required (uses only built-in `random` module).

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/amritxcode/blackjack-python.git
cd blackjack-python

2. Run the script:

python blackjack.py

Code Snippet:
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(deck)
