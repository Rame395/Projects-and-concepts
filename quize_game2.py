questions=("How many emement are there in periodic table?: ",
          "Which animal lays the largest eggs?: ",
          "What is the most abundant gas in Earth's atmosphere?: ",
          "How many bones are there in human body?: ",
          "Which planate in the solar system is the hottest?: ")

options=(("A.116" , "B.117", "C.118", "D.119"),
         ("A.Whale" , "B.Elephant", "C.Ostrich", "D.Eagle"),
         ("A.Oxygen" , "B.Nitrogen", "C.Carbon-dioxide", "D.Hydrogen"),
         ("A.206" , "B.345", "C.205", "D.346"),
         ("A.Earth" , "B.Venus", "C.Mars","D.Venus"))

answers=("C","C","B","A","C") 
guesses=[]
score=0
question_num=0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
      print(option)

    guess=input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
       score +=1
       print("CORRECT")
    
    

    else:
       print("INCORRECT")
       print(f"The correct answer is {answers[question_num]}")
    question_num +=1

print("-----------------")
print("           RESULT       ")
print("------------------")

print("answers:",end="")
for answer in answers:
   print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
   print(guess,end=" ")
print()


score= int(score/len(questions)*100)
print(f"Your score is: {score}%")


