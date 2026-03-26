def calculate_love_score(name1, name2):
    combined_name=(name1 + name2).lower()
    count = 0
    for letter in combined_name:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            count += 1
    love_letters= "love"
    count1 = 0
    for char in love_letters:
        for letter in combined_name:
            if letter == char:
                count1+=1
    
    love_score= str(count) + str(count1)
    print("Your love score is:",love_score)

def calculate_love_score(name1, name2):
    combined_name=(name1 + name2).lower()
    count = 0
    for letter in combined_name:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            count += 1
    love_letters= "love"
    count1 = 0
    for char in love_letters:
        for letter in combined_name:
            if letter == char:
                count1+=1
    
    love_score= str(count) + str(count1)
    print("Your love score is:",love_score)

calculate_love_score("Name1", "Name2")
