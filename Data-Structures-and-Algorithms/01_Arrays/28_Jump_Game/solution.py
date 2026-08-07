class solution:
    def canJump(self, nums):
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True

# Test
obj = solution()
nums = [3, 4, 2, 5, 0]
print(obj.canJump(nums))