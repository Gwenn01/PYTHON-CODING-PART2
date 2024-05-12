class Solution:
    def thirdMax(self, nums):
        # remove duplicates
        nums = list(set(nums))
        # if the length of nums is < 3
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        # if the nums length is 3 then
        max1 =  0
        max2 =  0
        max3 = 0
        for i in range(len(nums)):
            if nums[i] > nums[max1]:
                max1 = i
        nums[max1] = 0
        for i in range(len(nums)):
            if nums[i] > nums[max2]:
                max2 = i
        nums[max2] = 0
        for i in range(len(nums)):
            if nums[i] > nums[max3]:
                max3 = i
        return nums[max3]
            
solution = Solution()
nums = [1,1, 2]
print(solution.thirdMax(nums))