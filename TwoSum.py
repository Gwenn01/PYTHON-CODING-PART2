class Solution:
	def twoSum(self, nums, target):
		result = []
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				sum = nums[i] + nums[j]
				if sum == target:
					result.append(i)
					result.append(j)
					break
		return result
		
s = Solution()
nums = [2, 3, 4, 6, 8, 10]
target = 9
print(s.twoSum(nums, target))