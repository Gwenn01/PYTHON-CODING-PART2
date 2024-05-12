def numberToWords(n):
    words = ['too small', 'one', 'two', 'three', 'four', 'too large']
    if n < 1:
        return words[0]
    elif n < 5:
        return words[n]
    else:
        return words[5]
        
n = int(input('Enter Number: '))
print(numberToWords(n))
        
            