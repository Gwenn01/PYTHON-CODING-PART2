def findMissing(nums):
    missing_num = []
    number = 1
    last_num = nums[len(nums)-1]
    index = 0
    while number <= last_num:
        if number != nums[index]:
            missing_num.append(number)
            number += 1
        else:
            number += 1
            index += 1
    return missing_num
  
nums = [1, 2, 4, 6, 8, 9, 10]
print(findMissing(nums))
            
            