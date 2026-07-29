class solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

# Test
obj = solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 4
obj.rotate(nums, k)
print(nums)