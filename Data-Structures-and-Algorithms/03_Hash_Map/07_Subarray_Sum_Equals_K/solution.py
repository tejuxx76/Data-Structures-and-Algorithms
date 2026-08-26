num = [1, 2, 3, 2]
k = 2

count = 0

for i in range(len(num)):
    total = 0
    for j in range(i, len(num)):
        total = total + num[j]

        if total == k:
            count = count + 1
print("Number of subarrays:", count)