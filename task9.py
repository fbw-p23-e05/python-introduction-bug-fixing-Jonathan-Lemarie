
x = input("Type your value: ")

if x == '0':
    x = False   # x then become a Boolean false. if 0 was entered
elif x == '1':
    x = True
else:
    pass    # 

print("Your entered value is now", x)


# bugs was that values was received or entered as integer when they needed to be a string.