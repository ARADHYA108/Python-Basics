num = int(input("Enter a number."))

sum = 0

length = len(str(num))

temp = int (num) 

while temp > 0:
    digit = temp % 10
    sum = sum + digit**length
    temp//=10 

if num == sum:
    print( num , "is an Armstrong number.")
else:
    print( num , "is not an Armstrong number.")
