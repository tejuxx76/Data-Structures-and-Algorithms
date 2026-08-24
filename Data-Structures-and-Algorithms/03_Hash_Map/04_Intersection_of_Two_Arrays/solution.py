nums1 = [1, 2, 2, 1]
nums2 = [2, 3]

set1 = set(nums1)
result = []
for num in nums2:
    if num in set1 and num not in result:
        result.append(num)
print("Intersection:", result)