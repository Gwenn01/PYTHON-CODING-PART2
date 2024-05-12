def powerOfTwo(n):
    powerOf = 1
    while powerOf <= n:
        if powerOf == n:
            return True
        powerOf *= 2
    return False
    
print(powerOfTwo(256))