# Todo : make the coin-transaction

MENU = {
    "espresso": {
        "ingredients": {
            "water": 0,
            "milk": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

Capacity = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def report():
    print("\n\nThe report:\n")
    print(f"We have in the tank {Capacity['water']}ml water")
    print(f"We have in the tank {Capacity['milk']}ml milk")
    print(f"We have in the tank {Capacity['coffee']}g coffee")

def order():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    ingredients = MENU[choice]["ingredients"]

    missing = []
    enough = all(Capacity[item] >= amount_needed
                or missing.append(item) 
                for item, amount_needed in ingredients.items()
                )

    if enough :
        print(f"Here's your {choice}, have a nice day!")
        # sub from the tank
        for item, amount_needed in ingredients.items():
            Capacity[item] = Capacity[item] -  amount_needed
    else :
        print(f"Not enough {missing[0]}.")

    

working = True
print("\nWelcome to our new coffee machine!")
while working:


    print("\nType order to order")
    print("Type report to see report")
    print("Type exit to exit")

    userTyped = input("Type here: ")
    if userTyped == "exit" :
        working = False
    elif userTyped == "report" :
        report()
    elif userTyped == "order" :
        order()