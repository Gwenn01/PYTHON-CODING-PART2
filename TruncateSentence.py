class Solution:
    def truncateSentence(self, s, k):
        result = ""
        for str in s:
            if str == ' ':
                k -= 1
            if k == 0:
                break
            result += str
        return result
            
        
s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))
            