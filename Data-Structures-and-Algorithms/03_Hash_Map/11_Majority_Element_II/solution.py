nums = list(map(int, input("Enter numbers: ").split()))
result = []
for num in nums:

    if nums.count(num) > len(nums) // 3:
        if num not in result:
            result.append(num)
print("Majority Elements:", result)