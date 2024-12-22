foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food to buy or(q for quite): ")
    if food.lower()== "q":
        break
    else:
        price=float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("______YOUR CART_____")

for food in foods:
    print(food)

for price in prices:
    total +=price

print(f"Your total: ${total}")

print(" Thank you for visiting our resturant!")
