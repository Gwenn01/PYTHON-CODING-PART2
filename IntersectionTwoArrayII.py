class Solution:
    def intersection(self, nums1, nums2):
        intersec = []
        for num1 in nums1:
            for i in range(len(nums2)):
                if num1 == nums2[i]:
                    intersec.append(num1)
                    nums2.pop(i)
                    break
        return intersec
            
        
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2, 2]
print(s.intersection(nums1, nums2))