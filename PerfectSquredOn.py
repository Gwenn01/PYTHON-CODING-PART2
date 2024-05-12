class Solution:
    def isPerfectSquared(self, num):
        perfect_squared = 1
        index = 1
        while perfect_squared <= num:
            perfect_squared *= perfect_squared
            if perfect_squared == num:
                return True
            index += 1
            perfect_squared = index
        return False
        
s = Solution()
print(s.isPerfectSquared(14))