
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result > 15 and result < 20:   # it needs to be a 'and' instead of 'or'
    sum = 20
    print("Calculated sum is ", sum)
else:                                   # also added the ELse line to print other result.
    print('calculated sum is', result)