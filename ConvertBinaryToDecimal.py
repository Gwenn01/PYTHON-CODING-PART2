def convertDecimal(binary):
    result = 0
    binary = str(binary)
    index = len(binary)-1
    for b in binary:
        if b == '1':
            result += 2 ** index
        index -= 1
    return result
        
binary = int(input('Enter Binary: '))
print(f"Decimal: {convertDecimal(binary)}")