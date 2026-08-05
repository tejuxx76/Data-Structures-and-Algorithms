class solution :
    def setZeroes(self, matrix):
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for r in row:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in col:
            for i in range(len(matrix)):
                matrix[c][i] = 0

        return matrix
#test
obj =solution()
matrix = [[2,2,2],
          [2,0,1],
          [1,1,2]]
mat = obj.setZeroes(matrix)
for row in mat:
    print(row)