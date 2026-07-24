class solution :
    def maxSubarray(self,nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

#test
obj = solution()
nums = [1,3,4,-5,-7,9]
print(obj.maxSubarray(nums))