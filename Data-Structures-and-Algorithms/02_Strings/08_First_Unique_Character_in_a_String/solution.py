s = "tejas"

for i in range(len(s)):
    if s.count(s[i]) == 1:
        print("First unique character:", s[i])
        print("Index:", i)
        break
else:
    print("No unique character found")