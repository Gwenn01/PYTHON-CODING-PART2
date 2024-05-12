class Solution:
    def isPowerThree(self, n):
        if n == 1:
            return True
        if n < 3:
            return False
        index = 1
        while True:
            temp = 3 ** index
            if temp == n:
                return True
            if temp > n:
                return False
            index += 1
                
                
s = Solution()
print(s.isPowerThree(21))
            