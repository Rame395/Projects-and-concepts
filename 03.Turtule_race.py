import turtle
import time
import random

WIDTH,HIGHT=500,500
COLORS=["red","green","blue","orange","yellow","brown","black","purple","pink","cyan"]



def get_number_of_racers():
    racers=0
    while True:
        racers=input("Enter the number of racer (2 - 10): ")
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                break
            else:
                print("Number not in range. Please try again!")
        
        else:
            print("Input is not numberic.. Try again!")

    return racers
def race(colors):
    turtles=create_turtles(colors)

    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HIGHT//2-10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH // (len(colors) +1)
    for i ,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*spacingx,-HIGHT//2+20)
        racer.pendown()
        turtles.append(racer)

    return turtles

    


def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HIGHT)
    screen.title("TURTLE RACING!")

racers=get_number_of_racers()
init_turtle()

start_time=time.time()

random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)

end_time=time.time()
total_time=round(end_time-start_time,2)


print(f"The winner is the turtle with color:{winner} and take {total_time}seconds")
time.sleep(5)



def main():
    while True:
      play=input("press enter to play game or (q to quite): ")
      if play=="q":
          break
      

main()
      




        
    
            








