class Solution:
    def wordPattern(self, pattern, s):
        word = self.convertList(s)
        pOne = 0
        pTwo = len(pattern)-1
        while pOne < pTwo:
            if pattern[pOne] == pattern[pTwo]:
                if word[pOne] != word[pTwo]:
                    return False
            if pattern[pOne] != pattern[pTwo]:
               if word[pOne] == word[pTwo]:
                   return False
            pOne += 1
            pTwo -= 1
        for i in range(len(pattern)-1):
            if pattern[i] == pattern[i+1]:
                if word[i] !=word[i+1]:
                    return False
            if pattern[i] != pattern[i+1]:
                if word[i] == word[i+1]:
                    return False    
        return True       
        
    def convertList(self, s):
        word = []
        temp = ""
        for str in s:
            if str == " ":
                word.append(temp)
                temp = ""
            else:
                temp += str
        word.append(temp)
        return word
                
solution = Solution()
pattern = "aaaa"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))