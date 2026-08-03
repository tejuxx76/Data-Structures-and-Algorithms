class Solution:
    def findKthLargest(self, nums, k):

        nums.sort(reverse=True)

        return nums[k - 1]


# Test Code
obj = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(obj.findKthLargest(nums, k))