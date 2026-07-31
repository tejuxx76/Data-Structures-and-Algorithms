class solution:
    def sortColors(self, nums):
        nums.sort()
        return nums

# Test
obj = solution()
nums = [34, 12, 55, 2, 4, 23]

print(obj.sortColors(nums))