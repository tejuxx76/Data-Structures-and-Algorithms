class solution:
    def removeDuplicates(self, nums):

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# Test Code
obj = solution()

nums = [1, 1, 2]

k = obj.removeDuplicates(nums)

print("Unique Elements:", k)
print("Array:", nums[:k])