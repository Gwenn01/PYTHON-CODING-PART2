def gcd(x, y):
    res = 0;
    for i in range(1, y):
        if x % i == 0 and y % i == 0:
            res = i
    return res

num1 = int(input('Enter First Number: ')) 
num2 = int(input('Enter Second Number: '))      
print(f"GCD: {gcd(num1, num2)}")      
        