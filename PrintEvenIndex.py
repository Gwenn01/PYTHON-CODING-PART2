def printEvenIndex(str):
    result = []
    for i in range(len(str)):
        if i % 2 == 0:
            result.append(str[i])
    return result
    
str = "pynative"
ans = printEvenIndex(str)
print(ans)
    