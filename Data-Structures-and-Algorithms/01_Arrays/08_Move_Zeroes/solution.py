class solution:
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        while k < len(nums):
            nums[k] = 0
            k += 1

# test
obj = solution()
nums = [0, 5, 0, 2, 7]
obj.moveZeroes(nums)
print(nums)