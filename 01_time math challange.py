import random
import time

OPERATORS=["+","-","*"]
MAX_OPERAND=12
MIN_OPERAND=2
TOTAL_PROBLEMS=10

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operators=random.choice(OPERATORS)

    expr=str(left) +"" + operators + ""+ str(right)
    answer=eval(expr)
    return expr,answer



input("Press enter to start!")
print("---------------------------------")

start_time=time.time()
RIHGT=0

for i in range(TOTAL_PROBLEMS):
    expr, answer=generate_problem()
    while True:
      guess=input("problem#" + str(i+1) +"." +expr +"=")
      if guess==str(answer):
         break
      RIHGT +=1
      break
      
end_time=time.time()
total_time=round(end_time - start_time,2)

print("--------------------------------")
print(f"Nice Work!You finished in: {total_time} second and scored { RIHGT} out of 10")