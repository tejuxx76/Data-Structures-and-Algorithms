class solution:
    def findKthLargest(self, nums, k):

        nums.sort(reverse=True)

        return nums[k - 1]


# Test Code
obj = solution()

nums = [ 5, 6,3, 2, 1, 7]
k = 2
print(obj.findKthLargest(nums, k))