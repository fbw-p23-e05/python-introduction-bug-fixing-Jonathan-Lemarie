
x = input("Type your value: ")

if x == '0':
    x = 'False'
    print("Your entered value is now ", x)
elif x == '1':
    x = 'True'
    print("Your entered value is now ", x)
else:
#pass
    print("Your entered value is now ", x)


# bugs was that values was received or entered as integer when they needed to be a string.