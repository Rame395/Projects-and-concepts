#python slot machine
import random
import time

def spin_row():
    symbols=['🍒', '🍉', '🍋', '🔔' ,'⭐']

    # result=[]
    # for symbool in range(3):
    #     result.append(random.choice(symbols))
    # return result
    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-----------------")
    print(" | ".join(row))
    print("------------------")

def get_playout(row,bet):
    if row[0]==row[1]==row[2]:
        if row [0]=="🍒":
            return bet *3
        elif row [0]=="🍉":
            return bet *4
        elif row [0]=="🍋":
            return bet *5
        elif row [0]=="🔔":
            return bet *10
        elif row [0]=="⭐":
            return bet *30
    return 0
    

def main():
    balance=500
    print("--------------------")
    print("WELCOME TO MY SLOT MACHINE GAME!")
    print()
    print("Odd of winning")
    print("🍒:*3 🍉:*4 🍋:*5 🔔:*10 ⭐:*30")
    print()
    print("---------------------")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("---------------------")

    while balance>0:
        print(f"your current balance : ${balance}")

        bet= input("place yours bet amount:")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet=int(bet)

        if bet>balance:
            print("Insufficient Balance ")
            continue

        if bet<=0:
            print("Bet must be greater than 0")
            continue

        balance -=bet

        row=spin_row()
        print("spinning......\n")
        time.sleep(1)
        print_row(row)

        payout=get_playout(row , bet)

        if payout > 0:
            print(f"you won: ${payout}")
        else:
            print("Sorry you lost this round!,you can try again")

        balance +=payout

        play_again=input("Do you want to spin again? (Y/N):").upper()

        if play_again!="Y":
            break

    print(f"Game over! Your final balance is: ${balance}")



if __name__== '__main__':
    main()





    

    



