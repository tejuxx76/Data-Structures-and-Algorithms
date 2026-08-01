class solution:
    def findMaxAverage(self, nums, k):
        max_avg = float("-inf")
        for i in range(len(nums) - k + 1):
            total = sum(nums[i:i + k])
            average = total / k
            if average > max_avg:
                max_avg = average
        return max_avg
# Test
obj = solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(obj.findMaxAverage(nums, k))