def powerOfThree(n):
    powerOf = 1
    while powerOf <= n:
        if powerOf == n:
            return True
        powerOf *= 3
    return False
    
print(powerOfThree(27))