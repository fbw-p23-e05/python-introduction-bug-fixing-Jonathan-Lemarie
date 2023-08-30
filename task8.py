
x = float(input("First number: "))    # bug, one too many == just one = needed.
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))  # added max()
print("The minimum value is ", min(x, y ,z))   # corrected the abs with min()