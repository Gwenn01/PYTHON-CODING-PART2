class Solution:
    def intersec(self, nums):
        for i in range(1, len(nums)):
            nums[i] = self.intersecTwoArray(nums[i-1], nums[i])
        self.sortArray(nums[len(nums)-1] )
        return nums[len(nums)-1]
            
    def intersecTwoArray(self, nums1, nums2):
        result = []
        temp = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    result.append(num1)
                    break
        for r in result:
            if r not in temp:
                temp.append(r)
        return result
       
    def sortArray(self, nums):
        for i in range(len(nums)):
            for j in range(1, len(nums)-i):
                if nums[j-1] > nums[j]:
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
                
s = Solution()
nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
print(s.intersec(nums))
        