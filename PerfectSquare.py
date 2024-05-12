def perfectSquare(n):
    square, temp = 1, 1
    while temp <= n:
        temp = square * square
        if temp == n:
            return True
        square += 1
    return False
    
print(perfectSquare(4))