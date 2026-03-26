def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

logo = ''' 
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)
calculation = True
n1 = float(input("Enter first number: "))

while calculation is True:
    print("+\n-\n*\n/")
    operation_symbol = (input("Pick an operator: "))
    n2 = float(input("Enter second number: "))

    operation_function = operations[operation_symbol]
    result = operation_function(n1,n2)

    print(f"{n1} {operation_symbol} {n2} = {result}")

    further_calculations = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation, or type 'Q' to quit: ").lower()

    if further_calculations == "y":
        n1 = result
    elif further_calculations == 'n':
        print(logo)
        n1 = float(input("Enter first number: "))
    elif further_calculations == 'q':
        break