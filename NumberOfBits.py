def convert(n):
    res = ""
    while n != 0:
        if n % 2 == 0:
            res += '0'
        else:
             res += '1'
        n //= 2
    return res
    
def numBits(n):
    count = 0
    bits = convert(n)
    for bit in bits:        
        if bit == '1':
            count += 1
    return count
            
n = 15
ans = numBits(n)
print(ans)
   