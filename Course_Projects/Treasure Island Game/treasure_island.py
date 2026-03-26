print('''****************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____  
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_  
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____  
/______/______/______/______/______/______/______/______/______/______/______/__
*******************************************************************************''')
while True:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure without getting trapped or hurt.")

    c1 = input('You\'re at a crossroad, where do you want to go? Type "right" or "left": ').lower()

    if c1 == "left":
        c2 = input('You arrive at a lake. You see a boat, but it looks old. '
               'Type "wait" to wait for a new boat or "swim" to swim across: ').lower()
        if c2 == "wait":
            c3 = input("A boat arrives and takes you to an island with a house having 3 doors: red, yellow, and blue.\n"
                   "Which colour do you choose? ").lower()
            if c3 == "yellow":
               print("You found the treasure! Congratulations, you win!")
            elif c3 == "red":
                print("The room is full of fire. Game Over.")
            elif c3 == "blue":
                print("You enter a room with wild beasts. Game Over.")
            else:
                print("That door doesn't exist. You get lost. Game Over.")
        else:
            print("You tried to swim but got caught by crocodiles. Game Over.")
    elif c1 == "right":
        c4 = input("You fell into a hole! Do you want to try to climb out? Type 'yes' or 'no': ").lower()
        if c4 == "yes":
            print("You managed to climb out safely but got lost in the forest. Game Over.")
        else:
            print("You stayed in the hole forever. Game Over.")
    else:
        print("You hesitated too long and a wild animal found you. Game Over.")


    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break  # exit the loop and end the game
