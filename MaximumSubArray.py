import sys
class Solution:
	def maxSubArray(self, nums):
		length = len(nums)
		max_val = -sys.maxsize - 1
		sum = 0	
		for i in range(length):
			sum += nums[i]
			max_val = max(max_val, sum)		
			if sum < 0: sum = 0
		return max_val
		
					
s = Solution()
nums = [2,1,-3,4,-1,2,1,-5,4]
ans = s.maxSubArray(nums)	
print(ans)	
		