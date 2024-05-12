def removeFirstN(str, n):
    if n > len(str):
        return
    res =""
    for i in range(n, len(str)):
        res += str[i]
    return res
    
str = "pynative"
n = 4
ans = removeFirstN(str, n)
print(ans)
        