def squareRoot(n):
    number = 1
    sqrt = 0
    while sqrt < n:
        sqrt = number * number
        if sqrt == n:
            return number
        number += 1
  
print(squareRoot(16))