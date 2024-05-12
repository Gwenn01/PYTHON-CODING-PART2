class Solution:
    def countBits(self, n):
        ans = []
        for i in range(n+1):
            temp = self.countBinary(i)
            ans.append(temp)
        return ans
            
    def countBinary(self, n):
        binary = self.convertBinary(n)
        count = 0
        for b in binary:
            if b == "1":
                  count += 1
        return count
                  
    def convertBinary(self, n):
        result = ""
        while n != 0:
            rem = n % 2
            result += str(rem)
            n //= 2
        return result
        

s = Solution()
print(s.countBits(2))