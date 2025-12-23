
principle = 0
rate = 0
time = 0

while principle<=0:     
    principle = float(input("Enter the principle amount: "))
    if(principle<=0):
        print("Principle cant be negative or zero")

while rate<=0:
    rate = float(input("Enter the rate amount: "))
    if(rate<=0):
        print("Rate cant be negative or zero")

while True:
    time = int(input("Enter the time amount: "))
    if(time<=0):
        print("time cant be negative or zero")
    else:
        break
total = principle * pow((1 + rate/100),time)
print(f"Balance after {time} year/s: ${total:2f}")