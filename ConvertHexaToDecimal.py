def convertDecimal(hexa):
    result = 0
    hexa = str(hexa)
    index = len(hexa)-1
    for h in hexa:
        if h != '0':
            if h == 'A':
                result += (16 ** index)*10
            elif h == 'B':
                result += (16 ** index)*11
            elif h == 'C':
                result += (16 ** index)*12
            elif h == 'D':
                result += (16 ** index)*13
            elif h == 'E':
                result += (16 ** index)*14
            elif h == 'F':
                result += (16 ** index)*15
            else:
                result += (16 ** index)*int(h)
        index -= 1
    return result
        
hexa = input('Enter Hexademal: ')
print(f"Decimal: {convertDecimal(hexa)}")