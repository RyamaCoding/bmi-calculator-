print("Welcome to the Python Pizza Delivery service")
size = input("What size of pizza do you want? (S, M, L): ")
add_pepperoni = input("Do you want pepperoni? (Y/N): ")
extra_cheese = input("Do you want extra cheese? (Y/N): ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
Pepperoni_small = 2
Pepperoni_rest = 3
cheese = 1

bill = 0

if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
else: 
    bill += large_pizza

if add_pepperoni == "Y":
    if size == "S":
        bill += Pepperoni_small
    else:
        bill += Pepperoni_rest

if extra_cheese == "Y":
    bill += cheese

print(f"Your total bill is ${bill}")

