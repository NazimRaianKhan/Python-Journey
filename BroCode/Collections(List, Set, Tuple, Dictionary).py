# collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates OK
# Set = [] unordered and immutable. but Add/Remove OK. NO duplicates
# Tuple = [] ordered and unchangeable. Duplicates OK . Faster
# dictionary = a collection of {key:value} pairs
#              ordered, changeable, No duplicates  

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
print()

#---------------------DICTIONARY------------------------
print("----------------------DICTIONARY-------------------")

capitals = {"USA": "Washingtion D.C.",
            "Bangladesh": "Dhaka",
            "China": "Beijing",
            "Russia": "Moscow",}

#print(dir(capitals))  #shows all built in functions of a list
#print(help(capitals))

print(capitals.get("USA"))
if(capitals.get("Japan")):              # we get none as there is no japan
    print("That capital exists")
else:
    print("The capital doesnt exist.")

print(capitals)
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "LA"})           #add or edit a new key value pair
print(capitals)

capitals.pop("China")    #delete china
capitals.popitem()         #delete the last key:value pair
print(capitals)

keys = capitals.keys()  # to get all the keys in a dictionary not the values
print(keys)              # here keys is an object that resembles a list

for key in capitals.keys():
    print(key)

values = capitals.values()     # all same like the key
print(values)

for value in capitals.values():     
    print(value)

items = capitals.items()    #returns a dictionary object (2d list of tuples)
print(items)

for key,value in capitals.items():
    print(f"{key} : {value}")

capitals.clear()
print(capitals)