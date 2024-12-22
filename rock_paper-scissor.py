import random

option=["rock","paper","scissor"]
user_won=0
computer_won=0
while True:
    user_input=input("Type Rock/Paper/Sicissor or Q to quite;").lower()
    if user_input =="q":
        break
    if user_input not in option:
        continue

    random_number=random.randint(0,2)
    computer_picks=option[random_number]
    print(f"computer picks:{computer_picks}")

    if user_input =="rock" and computer_picks=="scissor":
        print("you won!")
        user_won +=1


    elif user_input =="paper" and computer_picks=="rock":
        print("you won!")
        user_won +=1

    elif user_input =="scissor" and computer_picks=="paper":
        print("you won!")
        user_won +=1
    
    else :
        print("computer won!")
        computer_won +=1

print(f"you won; {user_won} times")
print(f"computer won; {computer_won} times")
print("Thank you for playing my game")






