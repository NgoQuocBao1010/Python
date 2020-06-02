def differentSquares(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_2x2 = []
    list_of_2x2_matrices = []

    if rows < 2 and columns < 2:
        return 0

    elif rows == 2 and columns == 2:
        for row in range(rows):
            for column in range(columns):
                matrix_2x2.append(matrix[row][column])
        list_of_2x2_matrices.append(matrix_2x2)
        return len(list_of_2x2_matrices)

    else:
        row = 0
        while row < rows - 1:
            for column in range(columns - 1):
                matrix_2x2.append(matrix[row][column])
                matrix_2x2.append(matrix[row][column+1])
                matrix_2x2.append(matrix[row + 1][column])
                matrix_2x2.append(matrix[row + 1][column + 1])
                if matrix_2x2 not in list_of_2x2_matrices:
                    list_of_2x2_matrices.append(matrix_2x2)
                matrix_2x2 = []
            row += 1
        return len(list_of_2x2_matrices)


print(differentSquares([[9,9,9,9,9],   [9,9,9,9,9],   [9,9,9,9,9],   [9,9,9,9,9],   [9,9,9,9,9],   [9,9,9,9,9]]))