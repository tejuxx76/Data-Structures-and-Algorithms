n = 3
result = "1"
for i in range(n - 1):
    new_result = ""
    j = 0
    while j < len(result):
        count = 1
        while j + 1 < len(result) and result[j] == result[j + 1]:
            count += 1
            j += 1
        new_result += str(count) + result[j]
        j += 1
    result = new_result
print("Count and Say:", result)