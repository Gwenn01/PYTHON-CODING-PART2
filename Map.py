def map(func, array):
    res = []
    for arr in array:
        res.append(func(arr))
    return res

nums = [1, 2, 3, 4, 5]
def multiply(x):
    return x * 2
ans = map(multiply, nums)
print(ans)