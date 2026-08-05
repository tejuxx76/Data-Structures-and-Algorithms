rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)