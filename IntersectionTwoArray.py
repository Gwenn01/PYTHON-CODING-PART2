class Solution:
    def intersection(self, nums1, nums2):
        intersec = []
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    intersec.append(num1)
                    break
        for i in intersec:
            if i not in result:
                result.append(i)
        return result
            
        
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1, nums2))