class Solution:
    def finalString(self, s):
        string = ""
        for str in s:
            if str == 'i':
                string = self.reverseString(string)
            else:
                string += str
        return string
        
    def reverseString(self, s):
        result = ""
        for i in range(len(s)-1, -1, -1):
            result += s[i]
        return result
        
        
s = Solution()
print(s.finalString("poiinter"))