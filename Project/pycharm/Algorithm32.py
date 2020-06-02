def sudokuChecking(grid):
    count = 0
    list_of_nums = '0123456789'
    rows = len(grid)
    columns = len(grid[0])

    for row in grid:
        for value in row:
            if value in list_of_nums:
                if row.count(value) > 1:
                    return False

    lst_of_value = []
    for column in range(columns):
        for row in range(rows):
            if grid[row][column] in list_of_nums:
                if grid[row][column] in lst_of_value:
                    return False
                lst_of_value.append(grid[row][column])
        lst_of_value = []

    submatrices3x3 = []
    list_of_3x3 = []

    for row

    return True


print(sudokuChecking([[".","9",".",".","4",".",".",".","."],   ["1",".",".",".",".",".","6",".","."],   [".",".","3",".",".",".",".",".","."],   [".",".",".",".",".",".",".",".","."],   [".",".",".","7",".",".",".",".","."],   ["3",".",".",".","5",".",".",".","."],   [".",".","7",".",".","4",".",".","."],   [".",".",".",".",".",".",".",".","."],   [".",".",".",".","7",".",".",".","."]]))