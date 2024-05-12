def swapMinMax(nums):
    min = 0
    max = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[max]:
            max = i
        if nums[i] < nums[min]:
            min = i
    temp = nums[max]
    nums[max] = nums[min]
    nums[min] = temp
    
nums = [5, 7, 2, 3, 1]
print(nums)
print("Swap")
swapMinMax(nums)
print(nums)
    