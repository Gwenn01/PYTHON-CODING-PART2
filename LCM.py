def lcm(x, y):
    original_x = x
    original_y = y
    while(True):
        if x == y:
            break
        x += original_x
        if x > y:
            y += original_y
    return x
            
num1 = int(input('Enter First Number: ')) 
num2 = int(input('Enter Second Number: '))      
print(f"LCM: {lcm(num1, num2)}")