class solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Test Code
obj = solution()

nums = [2, 8, 7, 15]
target = 9

print(obj.twoSum(nums, target))