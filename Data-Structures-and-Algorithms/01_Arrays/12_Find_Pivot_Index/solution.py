class solution:
    def pivoteIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            left_sum = left_sum + nums[i]
#Test
obj = solution()
nums = [6, 5, 6, 3, 7, 1]
print(obj.pivoteIndex(nums))