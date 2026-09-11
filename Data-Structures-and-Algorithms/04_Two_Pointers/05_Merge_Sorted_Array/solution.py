nums1 = list(map(int, input("Enter nums1: ").split()))
m = int(input("Enter m: "))

nums2 = list(map(int, input("Enter nums2: ").split()))
n = int(input("Enter n: "))

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print("Merged Array:", nums1)