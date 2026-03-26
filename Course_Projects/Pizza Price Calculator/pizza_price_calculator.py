print("Welcome to Python Pizza Deliveries!")
size= input("What size pizza do you want? S, M or L: ").upper()
pepperoni=input("Do u want pepperoni on your pizza? Y or N: ").upper()
ex_cheese=input("Do u want extra cheese? Y or N: ").upper()

#Size
bill=0
if (size=="S"):
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Wrong input")

#pepp bill
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif pepperoni=="Y":
        if size == "M" or size == "L":
            bill+=3

#EX cheese
if ex_cheese=="Y":
    bill+=1

print("Your total bill is:",bill)
