def diamondNum(n):
    n += 1
    for i in range(1, n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(f"{j}", end="")
        for j in range(2, i+1):
            print(f"{j}", end="")
        print()
    n -= 1
    for i in range(1, n):
        for j in range(0, i+1):
            print(" ", end="")
        for j in range(n-i, 0, -1):
            print(f"{j}", end="")
        for j in range(2, (n-i)+1):
            print(f"{j}", end="")
        print()
        
    
n = 5
diamondNum(n)