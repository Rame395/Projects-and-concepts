#email=rameshshahi714
# @gmail.com

Email=input("Enter your Email: ")

username=Email[:Email.index("@")]
domain=Email[Email.index("@")+1:]

print(f"your user name is :{username} and domain is :{domain}")