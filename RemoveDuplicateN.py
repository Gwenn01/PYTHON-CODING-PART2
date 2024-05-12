def removeDupli(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res
    
nums = [1, 6, 2, 3, 6, 1, 2, 7]
print(nums)
nums = removeDupli(nums)
print(nums)