def missing(arr):
    num = 1
    for i in arr:
        if num != i:
            return num
        num += 1
    return 0

arr = [1, 2, 3, 4, 6, 7, 8]
print(missing(arr))