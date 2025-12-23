# indexing = accesing elements of a seq using [] (indexing operator)
#            [start : end : step]
# [ -> inclusive , ] -> exclusive

credit_numbers = "1234-5678-912"

print(credit_numbers[:4])  #1234 will print
print(credit_numbers[5:9])
print(credit_numbers[5:])
print(credit_numbers[-1])   #last digit , neg just make it start from last

print(credit_numbers[::2])  #every second char 

last_digits = credit_numbers[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse = credit_numbers[::-1]
print(reverse)



