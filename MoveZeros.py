class Solution:
    def moveZeros(self, nums):
        count_zero = 0
        result = []
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
            else:
                count_zero += 1
        for i in range(count_zero):
            result.append(0)
        for i in range(len(nums)):
            nums[i] = result[i]
                
        
        
s = Solution()
nums = [0,1,0,3,12]
s.moveZeros(nums)
print(nums)