class Solution:
	def firstUniqChar(self, s):
		for i in range(len(s)):
			isOne = True
			for j in range(len(s)):
				if s[i] == s[j] and i != j:
					isOne = False
					break
			if isOne:
				return i
		return -1
		
		
s = Solution()
string = "leetcode"
print(s.firstUniqChar(string))
				
				