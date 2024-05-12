class Solution:
	def spiralOrder(self, nums):
		spiral_list = []
		r = len(nums)-1
		c = len(nums[0])-1
		left = 0
		right = c
		top = 0
		bottom = r
		while left <= right and top <= bottom:
			for i in range(left, right+1):
					spiral_list.append(nums[top][i])
			top += 1
			for i in range(top, bottom+1):
					spiral_list.append(nums[i][right])
			right -= 1
			if top <= bottom:
				for i in range(right, left-1, -1):
					spiral_list.append(nums[bottom][i])
				bottom -= 1
			if left <= right:
				for i in range(bottom, top-1, -1):
						spiral_list.append(nums[i][left])
				left += 1				
		return spiral_list		

s = Solution()
nums = [[1, 2, 3]]
ans = s.spiralOrder(nums);
print(ans)