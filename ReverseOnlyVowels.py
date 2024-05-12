class Solution:
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        answer = list(s)
        reverse_con = []
        i = 0
        index = []
        #get index and vowels
        for ans in answer:
            for vow in vowels:
                if ans == vow:
                    reverse_con.append(ans)
                    index.append(i)
            i += 1
        #reverse
        reversed = self.reverseList(reverse_con)
        reversed = list(reversed)
        for i in range(len(reversed)):
            answer[index[i]] = reversed[i] 
        return "".join(answer)
       
    def reverseList(self, reverse):
        result = ""
        for i in range(len(reverse)-1, -1, -1):
            result += reverse[i]
        return result

                                                                 
s = Solution()
print(s.reverseVowels('aA'))