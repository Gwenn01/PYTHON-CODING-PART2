class Solution:
    def temp(self, p, nums, index,container):
        # base comdition
        if index == len(nums):
            # convert it again to nums before appending it to container
            convert_num = []
            for ans in p:
                hold = int(ans)
                convert_num.append(hold)
            container.append(convert_num)
            return
        # substring the first nums
        ch = nums[index]
        i = 0
        while i <= len(p):
            # the get the first and sencond in our ans
            first = p[0 : i]
            second = p[i : len(p)]
            conacatinate = first + ch + second
            # call the recursion
            self.temp(conacatinate, nums, index + 1, container)
            i += 1
                
    def permuteUnique(self, nums):
        container = []
        # convert the nums into str to easily permute
        num_str = ""
        for num in nums:
            num_str += str(num)
        self.temp("", num_str, 0, container)
        # remove the duplicat ans
        unique_list = []
        for con in container:
            if con not in unique_list:
                unique_list.append(con)
        
        return unique_list
        
        
solution = Solution()
nums = [1, 2, 3]
ans= solution.permuteUnique(nums)
print(ans)     