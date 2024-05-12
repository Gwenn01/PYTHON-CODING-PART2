class Solution:
	def findTheDifference(self, s, t):
		list_s = list(s)
		list_t = list(t)
		for str in list_s:
			if str in list_t:
				list_t.remove(str)
		return ''.join(list_t)		
		
s = Solution()
print(s.findTheDifference("a", "aa"))
