class Solution:
    def isPowerFour(self, n):
        if n == 1:
            return True
        if n < 4:
            return False
        index = 1
        while True:
            temp = 4 ** index
            if temp == n:
                return True
            if temp > n:
                return False
            index += 1
           
s = Solution()
print(s.isPowerFour(1024))     