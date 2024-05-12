class Solution:
	def FirstTwoCharacter(self, s):
		for i in range(len(s)):
			count = 0
			for j in range(len(s)):
				if s[i] == s[j]and i != j:
					count += 1
			if count == 1:
				return s[i]
		return s
		
s = Solution()
str = "abccbaacz"
print(s.repeatedCharacter(str))