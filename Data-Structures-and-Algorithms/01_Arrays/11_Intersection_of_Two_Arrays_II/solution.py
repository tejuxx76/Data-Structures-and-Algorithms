class solution:
    def intersect(self, nums1, nums2):

        result = []

        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result

# Test
obj = solution()

nums1 = [3, 1, 5, 2, 0, 1]
nums2 = [2, 5, 3, 2]

print(obj.intersect(nums1, nums2))