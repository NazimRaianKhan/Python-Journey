# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = [] unordered and immutable. but Add/Remove OK. NO duplicates
# Tuple = [] ordered and unchangeable. Duplicates OK . Faster

#-----------LIST---------------
print("----------------------LiST-------------------")
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[2])
print(fruits[0:3:2])
print(fruits[3::-1])
for fruit in fruits:
    print(fruit,end=" ")
print()

#print(dir(fruits))  #shows all built in functions of a list
#print(help(fruits)) #description of the built in mmethods

print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
print(fruits)

fruits.append("strawberry")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.insert(2,"banana")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("banana"))

print(fruits.count("banana"))

fruits.clear()
print(fruits)

#---------------------SET------------------------
print("----------------------SET-------------------")

fruits_set = {"apple", "orange", "banana", "coconut"}

#print(dir(fruits_set))  #shows all built in functions of a list
#print(help(fruits_set)) #description of the built in mmethods

print(len(fruits_set))
print("apple" in fruits_set)

#print(fruits_set[0])
#fruits_set[0] = "pineapple"   # cant do indexing in set as they are unordered
#print(fruits)

fruits_set.add("strawberry")
print(fruits_set)

fruits_set.remove("banana")
print(fruits_set)

fruits_set.pop()   #remove first element but it will be random
print(fruits_set)

fruits_set.clear()
print(fruits)

#---------------------TUPLE------------------------
print("----------------------TUPLE-------------------")

fruits_tuple = ("apple", "orange", "banana", "coconut")

#print(dir(fruits_tuple))  #shows all built in functions of a list
#print(help(fruits_tuple)) #description of the built in mmethods

print(len(fruits_tuple))
print("apple" in fruits_tuple)

print(fruits_tuple[0])
#fruits_tuple[0] = "pineapple"   # unchangable but ordered
print(fruits_tuple)

print(fruits_tuple.index("apple"))

print(fruits_tuple.count("coconut"))

for fruit in fruits_tuple:
    print(fruit, end=" ")


