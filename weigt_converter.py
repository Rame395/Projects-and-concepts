#python weight converter

weight=float(input("Enter your weight: "))
unit=input("Kilogram or Pound?(k or p):").lower()

if unit=="k":
    weight=weight*2.205
    unit="lbs"
    print(f"your weight is:{round(weight,1)}{unit}")
elif unit=="p":
    weight=weight/2.205
    unit="kgs"
    print(f"your weight is: {round(weight,1)} {unit}")
else:
    print(f"unit was invalid!")


