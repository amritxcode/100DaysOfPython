import random

stages = [
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       -
    """, # 0 Lives
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       -
    """, # 1 Life
    """
       --------
       |      |
       |      O
       |     /|
       |      
       -
    """, # 2 Lives
    """
       --------
       |      |
       |      O
       |      |
       |      
       -
    """, # 3 Lives
    """
       --------
       |      |
       |      O
       |    
       |      
       -
    """, # 4 Lives
    """
       --------
       |      |
       |      
       |    
       |      
       -
    """  # 5 Lives
]

print("Welcome to Hangman, the list contains states of India")
india_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

#Computer chooses and prints "_"
play_again = True
while play_again:
   chosen = random.choice(india_states).lower()
   blank =[]
   guessed_already= []
   for letter in chosen:
      if letter == " ":
         blank.append(letter)
      else:
         blank.append("_")
   print(" ".join(blank))

   #user guess and lives
   game_over = True
   lives = 5
   print("Lives:",lives)
   while game_over:

      guess = input("Enter a letter: ").lower().strip()
      found = False
      
      if guess in guessed_already:
          print(f"You already guessed {guess}.\n",end=",")
          continue
      guessed_already.append(guess)

      for i, letter in enumerate(chosen):
            if letter == guess:
               blank[i] = letter
               found = True

      if not found:
         lives -= 1
         print(f"Wrong guess. Lives left: {lives}")
         print(stages[lives])
         
      if "_" not in blank:
         print(f"You win!\nThe state was: {chosen.title()}")
         game_over = False

      elif lives==0:
            print("Game Over! You ran out of lives.")
            print(f"The state was: {chosen.title()}")
            game_over = False
      
      else:
         print(" ".join(blank))
   
   #player choice play or not
   play = input("Play again? (Y/N).\n").lower().strip()
   if play != 'y':
       play_again = False
       print("Thank you for playing!")
       