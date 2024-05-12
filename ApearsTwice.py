class Solution:
	def repeatedCharacter(self, s):
		list_range = []
		for i in range(len(s)):
			r = 0
			isOne = True
			count = 0
			for j in range(len(s)):
				if s[i] == s[j]:
					count += 1
			if count < 3:					
				for j in range(i+1, len(s)):
					if s[i] == s[j]:
						isOne = False
						break
					r += 1
			if isOne or r == 0:
				list_range.append(len(s))
			else:
				list_range.append(r)
				
		return s[self.findSmall(list_range)]
				

	def findSmall(self, range_list):
		min = len(range_list)-1
		for i in range((len(range_list)-1), 0, -1):
			if range_list[i-1] < range_list[i]:
				min = i-1
		return min
							
s = Solution()
str = "tahhplthue"
print(s.repeatedCharacter(str))