def isDuplicate(arr):
    for i in range(len(arr)):
        split_range = i+1
        if arr[i] in arr[split_range:]:
            return True
    return False
       

arr = [2, 3, 3]
print(isDuplicate(arr))
