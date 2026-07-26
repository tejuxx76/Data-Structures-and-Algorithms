class solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key in count:
            if count[key] > len(nums) // 2:
                return key

# Test
obj = solution()

nums = [3, 6, 4, 3, 6, 3, 7,1,1,1,1,3,  3]

print(obj.majorityElement(nums))