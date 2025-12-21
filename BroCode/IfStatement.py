############ If Statements ################

age = int(input("Enter your age: "))

if age>=18 and age<100:
    print("You are now signed up!")
elif(age<0):
    print("You havent been born yet.")
elif(age>=100):
    print("You are too old to sign up.")
else:
    print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N)")

if(response == "Y"):
    print("Have some food!")
else:
    print("No food for you")

name = input("Enter your name: ")
if(name==""):
    print("You didnt write your name")
else:
    print(f"Hello {name}")

for_sale = True
if(for_sale):
    print("This item is for sale")
else:
    print("This item is not for sale")