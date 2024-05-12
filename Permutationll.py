class Solution:
    def temp(self, p, nums, container, index):
        # base condition, if we find ans
        if index == len(nums):
            container.append(p.copy())
            return
        # to what value we have
        ch = nums[index]
        i = 0
        while i <= len(p):
            # first second in our p
            first = p[:i]
            second = p[i:]
            # concate the list
            new_p = first + [ch] + second
            # recursion call
            self.temp(new_p, nums, container, index+1)
            i += 1
                    
    def permutationll(self, nums):
        # container for ans
        container = []
        # helper function
        self.temp([], nums, container, 0)
        # remove the duplicate ans
        con_unique = []
        for con in container:
            if con not in con_unique:
                con_unique.append(con)
        return con_unique


solution = Solution()
nums = [1, 2, 3]
ans = solution.permutationll(nums) 
print(ans)       