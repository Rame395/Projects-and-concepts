unit=input("Is this temperature is in celsius/ Fahrehenit? (c/f):").lower()
temp=float(input("Enter the temperature:"))

if unit=="c":
    temp=round((9*temp)/5+32,1)
    print(f"Your temperature in fahrehenit is; {temp} degree fhrehenit")

elif unit=="f":
    temp=round((temp - 32) * 5/9,1)
    print(f"your temperature in celcius is; {temp} degree celcius")

else:
    print(f"{unit} is an invalid unit of temperature ")