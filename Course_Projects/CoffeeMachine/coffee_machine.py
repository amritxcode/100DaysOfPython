def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

menu = {
    "espresso":{
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}
    
resources ={
    "water":300,
    "milk":200,
    "coffee":100,
    "money": 0,
}

while True:
    choice = input("What would you like to have? (Espresso/Latte?Cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice in menu:
        drink = menu[choice]
        ingredients = drink["ingredients"]
        enough = True

        for item in ingredients:
            if ingredients[item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                enough = False
                break

        if enough:
            payment= process_coins()
            cost = drink["cost"]
            if payment < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                
                for item in ingredients:
                    resources[item] -= ingredients[item]
                resources["money"] += cost
                print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid input. Please choose espresso, latte, or cappuccino.")