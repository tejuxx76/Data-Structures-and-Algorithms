class solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]

# Test
obj = solution()
nums = [34, 53, 23, 67, 33, 99]
print(obj.thirdMax(nums))