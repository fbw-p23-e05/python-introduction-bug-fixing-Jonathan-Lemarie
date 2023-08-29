x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:   # bug, 2 times % , only 1 needed also need DBL =
    print("First number is divisible by second number, result =", x // y)
elif y % x == 0:   #  # bug, 2 times % , only 1 needed ,  also needs to be y % x
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisable!")