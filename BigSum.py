def bigSum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
    
nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(bigSum(nums))