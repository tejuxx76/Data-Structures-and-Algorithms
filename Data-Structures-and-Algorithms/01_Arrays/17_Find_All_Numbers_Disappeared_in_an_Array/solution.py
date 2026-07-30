class solution:
    def findDisappearedNumbers(self, nums):

        result = []
        n = max(nums)
        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)
        return result

# Test Code
obj = solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1, 12]
print(obj.findDisappearedNumbers(nums))