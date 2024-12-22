import random

n=int(input("Enter a number: "))

print("--------------")
if n<=0:
    print("Please enter a number larger than 0 from next time:")

else:
    print("You are good to play game")

random_number=random.randint(0,n)
guesses=0
print(f"make a guess between: 0 to {n}")
print("----------------")


while True:
    guesses =guesses + 1
    user_guess=int(input("Make a guesses:"))
    
    if user_guess==random_number:
        print("You got it!")
        break
    elif user_guess>random_number:
        print("you are above the number!")

    else:
        print("you are below the number!")
        # guesses =guesses + 1

print(f"You got it into {guesses} guesses!")



   
    
    
       



