# (1)open https://sudoku.com/ar/khabir/
# (2)enter the first row as string - with no spaces - from left to right
# (3) repeat (2) for each row



def findNextEmpty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None


def isValid(puzzle, guess, row, col):
    if guess in puzzle[row]:
        return False
    if guess in [puzzle[i][col] for i in range(9)]:
        return False
    startRow = row // 3 * 3
    startCol = col // 3 * 3
    if guess in [puzzle[r][c] for r in range(startRow, startRow + 3) for c in range(startCol, startCol + 3)]:
        return False
    return True


def solveSudoku(puzzle):
    row, col = findNextEmpty(puzzle)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solveSudoku(puzzle):
                return True
        puzzle[row][col] = 0
    return False


example = []

for i in range(9):
    l = []
    inp = input()
    for i in inp:
        l.append(int(i))
    example.append(l)

print("\n")
solution = solveSudoku(example)
if solution:
    print(example)
else:
    print("Error")
