class Solution:
	def removeSpace(self, str):
		res = ""
		for s in str:
			if s != " ":
				res += s
		return res.lower()

	def isAnagram(self, s, t):
		s = self.removeSpace(s)
		t = self.removeSpace(t)
		if len(s) != len(t):
			return False
		s_list = list(s)
		t_list = list(t)
		i = 0
		for n in range(len(s_list)):
			j = 0
			for m in range(len(t_list)):
				if s_list[i] == t_list[j]:
					s_list.pop(i)
					t_list.pop(j)
					i -= 1
					break
				j += 1
			i += 1
		return len(s_list) == 0			
					
sol = Solution()
s = "aacc"
t = "ccca"
ans = sol.isAnagram(s, t)
print(ans)