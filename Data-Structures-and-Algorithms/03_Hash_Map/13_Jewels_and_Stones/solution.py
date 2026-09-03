jewels = input("Enter jewels: ")
stones = input("Enter stones: ")
count = 0
for stone in stones:
    if stone in jewels:
        count += 1
print("Number of jewels:", count)