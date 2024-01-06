import menu as m
import re
flag = False;

def report():
    print(m.reporte)
    print(f"Water: {m.resources['water']} ml")
    print(f"Milk: {m.resources['milk']}")
    print(f"Coffee: {m.resources['coffee']}")
def giveDrink(name):
    print(f"Your {name} is ready")

    #decrements the resources from the machine when ,making coffee
def makeCoffee(ingredients):
    for ingredient in ingredients:
        m.resources[ingredient] -= ingredients[ingredient]
    

#drink ingredients es un dict  que tiene los ingredientes de cierta bebida

#return true if the machine have enoucgh ingredients
def checkResourcesFor(drink_ingredients):
    enough = True
    #para cada ingrediente (key) en los ing de la bebida
    for ingredient in drink_ingredients:
        #si la bebida requiere mas ing de lo que se tiene, entonces no hay suf
        #ingredientes
        if drink_ingredients[ingredient] > m.resources[ingredient]:
            enough = False
    return enough        

while(not flag):
    money = 0.0
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    valid_choice = re.compile(r'(es*p*r*e*s*s*o*|la*t*t*e*|ca*p*p*u*c*c*i*n*o*)')
    if not valid_choice.search(user_choice) or user_choice == 'off':
        print("Invalid option, shutting down")
        flag = True
    elif user_choice == "report":
        report()
    else:
        # TODO 
        #convert the user input to the key of dictionary
        #convert(user_choice)

        #obtain the drink info; contains ingredients and cost
        drink = m.MENU[user_choice]
        # 
        if not checkResourcesFor(drink["ingredients"]):
            print("Sorry, not enough ingredients")
        else: 
            print(f"Insert {drink['cost']} dollars")
            #user will enter coins until reaches or exced the price 

            #ends loop when money exceed cost
            while (money < drink['cost']):
                money += float(input("Enter coin:"))
                print(f"Current credit: {money}")
            if money > drink['cost']:
                change = money - drink["cost"]
                print(f"your change is {change}")
            makeCoffee(drink["ingredients"])
            giveDrink(user_choice)




