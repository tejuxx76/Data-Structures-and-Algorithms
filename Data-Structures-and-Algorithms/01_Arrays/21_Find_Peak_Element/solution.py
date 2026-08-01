class solution:
    def findPeakElement(self, nums):
        for i in range(len(nums)):
            left = nums[i - 1] if i > 0 else float("-inf")
            right = nums[i + 1] if i < len(nums) - 1 else float("-inf")
            if nums[i] > left and nums[i] > right:
                return i
# Test
obj = solution()
nums = [1, 2, 3, 4, 6, 1]
print(obj.findPeakElement(nums))