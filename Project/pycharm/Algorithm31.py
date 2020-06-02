
def spiralNUmbers(n):
    rpointer = 0
    cpointer = 0
    rows = n
    columns = n
    number = 1

    recent_number = 0
    result_list = [[None for column in range(columns)] for row in range(rows)]

    while True:

        for column in range(cpointer, columns):
            result_list[rpointer][column] = number
            number += 1
        rpointer += 1

        if number >= n * n + 1:
            break

        for row in range(rpointer, rows):
            result_list[row][columns - 1] = number
            number += 1

        if number >= n * n + 1:
            break

        columns = columns - 1
        column = columns - 1
        while column >= cpointer:
            result_list[rows - 1][column] = number
            number += 1
            column -= 1

        if number >= n * n + 1:
            break

        rows = rows - 1
        row = row - 1
        while row >= rpointer:
            result_list[row][cpointer] = number
            number += 1
            row -= 1
        cpointer += 1
        if number >= n * n + 1:
            break

    return result_list



print(spiralNUmbers(5))