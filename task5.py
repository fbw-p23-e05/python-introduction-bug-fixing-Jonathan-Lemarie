
x = int(input("First number: "))
y = int(input("Second number: "))     # but also need to add int()
z = int(input("Third number: "))   #   1st bug, one too many parenthesis

if x == y or y == z or x == z:   # 2nd bug =  should be ==    //      forgot the x == z
    result = 0
else:
    result = x + y + z    # argument as 'result' instead of 'sum'
print("Calculated sum is ", result)
