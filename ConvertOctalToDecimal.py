def convertDecimal(octal):
    result = 0
    octal = str(octal)
    index = len(octal)-1
    for o in octal:
        if o != '0':
            result += (8 ** index) * int(o)
        index -= 1
    return result
        
octal = int(input('Enter Octal: '))
print(f"Decimal: {convertDecimal(octal)}")