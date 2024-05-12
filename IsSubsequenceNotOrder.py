class Solution:
	def isSubsequence(self, s, t):
		list_t = list(t)
		for char in s:
			if char not in list_t:
				return False
			list_t.remove(char)
		return True
		
s = Solution()
print(s.isSubsequence("acb",
"ahbgdc"))