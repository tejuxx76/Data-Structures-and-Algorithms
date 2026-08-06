class solution:

    def rotate(self, matrix):
        n = len(matrix)

        new_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[n - 1 - j][i])
            new_matrix.append(row)
        return new_matrix
# Test
obj = solution()
matrix = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]
result = obj.rotate(matrix)
print("Rotated Matrix:")
for row in result:
    print(row)