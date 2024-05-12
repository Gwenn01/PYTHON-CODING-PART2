class Solution:
    def applyOperation(self, nums):
        pointer_one = 0
        pointer_two = 1
        while pointer_two < len(nums):
            if nums[pointer_one] == nums[pointer_two]:
                multiply = nums[pointer_one] * 2
                nums[pointer_one] = multiply
                nums[pointer_two] = 0
                pointer_one += 2
                pointer_two += 2
            else:
                pointer_one += 1
                pointer_two += 1
        self.moveZeros(nums)
        return nums          
                
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
nums = [1,2,2,1,1,0]
print(s.applyOperation(nums))