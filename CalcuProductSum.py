def calculate(num1, num2):
    product = num1 * num2
    sum = num1 + num2
    if product < 1000:
        return product
    return sum
   
num1 = 40
num2 = 30
ans = calculate(num1, num2)
print(ans)