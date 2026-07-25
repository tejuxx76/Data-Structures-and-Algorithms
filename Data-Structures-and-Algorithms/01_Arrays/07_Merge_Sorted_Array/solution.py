class solution:
    def merge(self, nums1, m, nums2, n):

        nums1[:] = sorted(nums1[:m] + nums2)


# Test
obj = solution()

nums1 = [1, 2, 4, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

obj.merge(nums1, m, nums2, n)

print(nums1)