n = 19
seen = set()
while n != 1:
    if n in seen:
        print("Not a Happy Number")
        break
    seen.add(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10
    n = total
else:
    print("Happy Number")