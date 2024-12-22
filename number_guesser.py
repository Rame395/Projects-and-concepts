import random

n=int(input("ENTER A NUMBER: "))

if n<=0:
    print("please enter a number larger than 0 next time.")
else:
    print("you are good to play game")

random_number=random.randint(0,n)
guesses=0

while True:
    guesses=guesses+1
    user_guess=int(input("make a guess; "))
    
    if user_guess==random_number:
        print("you got it!")
        break
    elif user_guess>random_number:
        print("you are above the number!")
    else:
        print("you are below the number!")

print(f"you got it into : {guesses} guesses")
      
    
    
    
        
