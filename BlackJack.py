def blackJack(a, b):
    sum = a + b
    if sum > 21:
        return 0
    return sum
        
    
a = int(input("Enter first card: "))
b = int(input("Enter second card: "))
print(blackJack(a, b))