def powerOfAnother(n, x):
    if n == 1:
        return True
    square = x
    while square <= n:
        if square == n:
            return True
        square = square * x
    return False
    
print(powerOfAnother(64, 2))