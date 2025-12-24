# FOR LOOP

for x in range(1,11):      #stop is exclusive
    print(x)

print("Happy new year")

for x in reversed(range (1,11)):
    print(x)

print("Happy new year")

for x in range(1, 11, 2):
    print(x)

print("Happy new year")

credit_card = "1234-5678-1245-5757"

for x in credit_card:
    print(x)

print("Happy new year")

for x in range(10, 21):
    if(x==13):
        continue
    elif(x==18):
        break
    else:
        print(x)