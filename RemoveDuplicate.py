def remove_dupli(nums):
    result = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                nums[i] = 0
    for num in nums:
        if num != 0:
            result.append(num)
    nums = result[:]
    return nums
   
nums = [1, 6, 8, 2, 5, 1, 6, 9, 4, 2]
print(nums)
nums = remove_dupli(nums)
print(nums)