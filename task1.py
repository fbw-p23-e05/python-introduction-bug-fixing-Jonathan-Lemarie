
three_mul = 'fizz'    # 1bug missing upper'
five_mul = 'buzz'
num1 = 3
num2 = 5     # 5th bug  was on wrong number 4 instead of 5
max_number = 100     # 2nd bug  was written max_num then the range would not find ..
   
for i in range(1,max_number):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:   # 6th bug this one should appear first or the fizzbuzz would not appear  , maybe 7th bug with the print line that needs to go with
        print(i, three_mul + five_mul)   # 4th bug for the print indentation
    elif i%num1 == 0:   # 3rd bug  missing an equal sign , needed 2.
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)