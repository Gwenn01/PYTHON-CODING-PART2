def addDigits(number):
    sum = number
    while sum > 9:
        temp = sum
        rem_sum = 0
        while temp != 0:
            rem = temp % 10
            rem_sum += rem
            temp //= 10
        sum = rem_sum
    return sum
            
number = 48
print(addDigits(number))