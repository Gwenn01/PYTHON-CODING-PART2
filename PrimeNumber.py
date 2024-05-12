def primeNum(n):
    print(f"{2}\n{3}\n{5}")
    for i in range(6, n+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
               print(i)
               

n = 20
primeNum(n)                
