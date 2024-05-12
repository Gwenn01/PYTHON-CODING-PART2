def evenOdd(n):
    two = 0
    while two <= n:
        if two == n:
            return "Even"
        two += 2
    return "Odd"
    

for i in range(100):  
    print(f"{i}: {evenOdd(i)}")