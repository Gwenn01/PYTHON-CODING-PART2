def returnNegative(n):
    if n <= 0:
        return n
    negative = 0
    while n != 0:
        negative -= 1
        n -= 1
    return negative
    
print(returnNegative(100))