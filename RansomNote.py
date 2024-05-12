class Solution:
	def canConstruct(self, ransomNote, magazine):
		ranList = list(ransomNote)
		for m in magazine:
			for i in range(len(ranList)):
				if m == ranList[i]:
					ranList.pop(i)
					break
		return len(ranList) == 0
		
s = Solution()
ransomNote = "aa"
magazine = "aba"
print(s.canConstruct(ransomNote, magazine))