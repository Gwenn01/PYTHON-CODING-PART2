def tipCalculator(a, b):
    if b == 1:
        return a * 0.05
    elif b == 2:
        return a * 0.1
    elif b == 3:
        return a * 0.15
    elif b == 4:
        return a * 0.2
    elif b == 5:
        return a * 0.25

a = int(input("Enter the amount: "))
b = int(input("Enter quality: "))
print(tipCalculator(a, b))