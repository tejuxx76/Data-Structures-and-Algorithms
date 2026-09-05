numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]
    if total == target:
        print("Indexes:", left + 1, right + 1)
        break
    elif total < target:
        left += 1
    else:
        right -= 1