
a = input("First value: ")   # need to add the input function and take off the 'int'
b = input("Second value: ")

print("Before swapping: a =", a, " ,b =", b)

temp = a
a = b
b = temp   # added this line
print("After swapping: a =", a, " ,b =", b)  # correct the syntax so so a and b are not just string text but arguments.