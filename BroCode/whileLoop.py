name = input("Enter your name: ")

while name == "":
    print("you did not enter a name")
    name = input("Enter your name: ")

print(f"Hello {name}")
