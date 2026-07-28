class solution:
    def missingNumber(self, nums):

        n = len(nums)
        total = n * (n + 1) // 2
        current = sum(nums)
        return total - current

# Test
obj = solution()

nums = [3, 5, 2, 0, 4]

print(obj.missingNumber(nums))