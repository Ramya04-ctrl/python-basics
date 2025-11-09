num = int(input("Enter a number: "))

while num >= 10:
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10
    num = sum

print( num)
