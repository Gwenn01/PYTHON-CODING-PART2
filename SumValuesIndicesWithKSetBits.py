class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        sum = 0
        length = len(nums)
        for i in range(length):
            if self.countBinary(i) == k:
                sum += nums[i]
        return sum
            
    def countBinary(self, n):
        binary = self.convertBinary(n)
        count = 0
        for b in binary:
            if b == "1":
                count += 1
        return count
        
    def convertBinary(self, n):
        result = ""
        while n != 0:
            rem = n % 2
            result += str(rem)
            n //= 2
        return result
        
s = Solution()
nums = [2, 2]
k = 1
ans = s.sumIndicesWithKSetBits(nums, k)
print(ans)