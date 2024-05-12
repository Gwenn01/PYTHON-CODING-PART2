class Solution:
    def reverseOnlyLetters(self, s):
        answer = ""
        i = 0
        result = self.convert(s)
        result = self.reverseString(result)
        for str in s:
            if not self.isAlpha(str):
               answer += str
            else:
               answer += result[i]
               i += 1
        return answer
     
    def isAlpha(self, letter):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for a in alpha:
            if a == letter or a.upper() == letter:
                return True
        return False
        
    def convert(self, s):
        result = ""
        for str in s:
            if self.isAlpha(str):
                result += str
        return result
        
    def reverseString(self, s):
        result = ""
        for i in range(len(s)-1, -1, -1):
            result += s[i]
        return result
              
s = Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))