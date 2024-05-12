class Solution:
    def majorityElement(self, nums):
        length = len(nums)
        if length % 2 != 0:
            length += 1
        length //= 2
        elements = set(nums)
        tempElements = list(elements)
        for elem in tempElements:
            count = 0
            for n in nums:
                if n == elem:
                    count += 1
            if count >= length:
                return elem
    
nums = [8,8,7,7,7]
s = Solution()
print(s.majorityElement(nums))