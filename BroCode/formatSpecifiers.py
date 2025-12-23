# format specifier = {value:flag} format a value based on what flags 
#                            are inserted

#.(number)f = round to that many deciaml places(fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad thay many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate postive value if it is positive
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 1200.3456

print(f"price 1 is ${price1:.2f}")
print(f"price 1 is {price2:.1f}")
print(f"price 1 is {price3:.0f}")

print(f"price 1 is {price1:10}")

print(f"price 1 is {price1:010}")

print(f"price 1 is {price1:<10}")

print(f"price 1 is {price1:>10}")

print(f"price 1 is {price1:^10}")

print(f"price 1 is {price1:+}")
print(f"price 1 is {price2:+}")

print(f"price 1 is {price2:=}")

print(f"price 1 is {price1: }")

print(f"price 1 is {price3:,}")

print(f"price 1 is {price3:+,.2f}")


