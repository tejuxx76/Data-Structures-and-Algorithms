class Solution:
    def sortedSquares(self, nums):
        result = []
        for num in nums:
            result.append(num * num)
        result.sort()
        return result

# Test
obj = Solution()
nums = [3, 2, 4, 1]
print(obj.sortedSquares(nums))