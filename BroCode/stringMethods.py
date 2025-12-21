name = input("Enter your full name: ")

print(len(name));    #length of string

print(name.find(" "))    #first occurance of char
print(name.find("n"))

print(name.rfind("n"))    #last occurance of char

print(name.capitalize())   #only first char is capitalized of the string

print(name.upper())     # all char capital
 
print(name.lower())     #all char lower

print(name.isdigit())    #returns true only if digits

print(name.isalpha())   ##returns true only if alphabetical char

print(name.count("n"))   #returns the num of char within a string

print(name.replace("n","m"))   #replaces a char with another char

print(help(str))


######## Validate user input Assignment ##############

# 1. username no more than 12 char
# 2. username must not contain spaces
# 3. username must not contain digits



