
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number   # bug was 1 instead of number variable
    number = number + 1
print("Sum =", sum)