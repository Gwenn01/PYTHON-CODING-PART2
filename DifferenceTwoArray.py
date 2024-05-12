class Solution:
    def findDifference(self, nums1, nums2):
        result = []
        difOne = []
        difTwo = []
        for num1 in nums1:
            isExist = False
            for num2 in nums2:
                if num1 == num2:
                    isExist = True
                    break
            if not isExist:
                difOne.append(num1)
        for num2 in nums2:
            isExist = False
            for num1 in nums1:
                if num2 == num1:
                    isExist = True
                    break
            if not isExist:
                difTwo.append(num2)
        result.append(self.removeDup(difOne))
        result.append(self.removeDup(difTwo))
        return result
       
    def removeDup(self, array):
        result = []
        for a in array:
            if a not in result:
                result.append(a)
        return result
        
s = Solution()
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(s.findDifference(nums1, nums2))