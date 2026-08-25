board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

valid = True

# Check rows
for row in board:
    numbers = set()

    for num in row:
        if num != ".":
            if num in numbers:
                valid = False
                break
            numbers.add(num)
# Check columns
for j in range(9):
    numbers = set()
    for i in range(9):
        num = board[i][j]
        if num != ".":
            if num in numbers:
                valid = False
                break
            numbers.add(num)
# Check 3 × 3 boxes
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        numbers = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                num = board[i][j]
                if num != ".":
                    if num in numbers:
                        valid = False
                        break
                    numbers.add(num)
print("Valid Sudoku:", valid)