first = input("Enter first intervals: ")
second = input("Enter second intervals: ")

first_list = eval(first)
second_list = eval(second)
result = []
i = 0
j = 0

while i < len(first_list) and j < len(second_list):

    start = max(first_list[i][0], second_list[j][0])
    end = min(first_list[i][1], second_list[j][1])

    if start <= end:
        result.append([start, end])
    if first_list[i][1] < second_list[j][1]:
        i += 1
    else:
        j += 1

print("Intersection:", result)