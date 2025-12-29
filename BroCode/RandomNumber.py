import random

#print(help(random))

low = 1
high = 100
number1 = random.randint(low, high)    #random num between 1 and 100
number2 = random.random()     #random float point , takes no argument

print(number1)
print(number2)

options = ("rock","paper","scissors")
option = random.choice(options)     #chooses random option
print(option)     

cards = ["1","2","3","4","5","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)