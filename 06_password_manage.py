import random
import string

def generate_password(min_len,numbers=True,special_character=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    character=letters
    if numbers:
        character +=digits
    if special_character:
        character +=special

    pwd=""
    meets_criteria=False
    has_numbers=False
    has_special=False

    while not meets_criteria or len(pwd)<min_len:
        new_char=random.choice(character)
        pwd +=new_char

        if new_char in digits:
            has_numbers=True
        elif new_char in special:
            has_special=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_character:
            meets_criteria=meets_criteria and has_special

    return pwd
while True:
  min_length=int(input("Enter minimum length of your password:"))
  has_numbers=input("Do you want to add number in your password (y/n)?:").lower()=="y"
  has_special=input("Do you want to add any special character in your password (y/n)?:").lower()=="y"
  pwd=generate_password(min_length,has_numbers,has_special)
  print(f"Your generated password is ;{pwd}")

  generate_password_again=(input("Do you want to generate password again? (y/n)?:")).lower()
  if generate_password_again!="y":
       break
print(f"Your final password is;{pwd}")
   

    



 

