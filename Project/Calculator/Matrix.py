
def create_matrix(rows, columns, lst):
    if rows * columns != len(lst):
        return
    matrix = []
    row = []
    for element in lst:
        row.append(element)

        if len(row) == columns:
            matrix.append(row)
            row = []

    return matrix


def display_matrix(mat):
    if max == None:
        print('Invalid Matrix')

    rows = len(mat)
    columns = len(mat[0])

    for row in range(rows):
        for column in range(columns):
            element = str(round(mat[row][column], 2))
            text = '{: ^6}'.format(element)
            if column == columns - 1:
                if row == rows - 1:
                    print(text)
                else:
                    print(text + '\n' + '=========' * columns)
            else:
                print(text + ' ||', end='')


def is_echelon_form(mat):
    if mat == None:
        return False

    rows = len(mat)
    columns = len(mat[0])

    if mat[0].count(0) == columns:
        return False
    else:
        for column in range(columns):
            if mat[0][column] != 0:
                indicator = column
                break

    row = 1
    while row < rows:
        for column in range(columns):
            if mat[row][column] != 0:
                if column <= indicator:
                    return False
                indicator = column
                break
        row += 1

    return True


def find_indicator(row):
    for column in range(len(row)):
        if row[column] != 0:
            return column
    return 1000


def sort_mat(mat):
    rows = len(mat)
    columns = len(mat[0])

    for row in range(rows - 1):
        r = row + 1
        while r < rows:
            if find_indicator(mat[row]) > find_indicator(mat[r]):
                mat[row], mat[r] = mat[r], mat[row]
            r += 1
    return mat


def echelon_form(maxt):
    rows = len(maxt)
    columns = len(maxt[0])

    if is_echelon_form(maxt):
        return maxt

    maxt = sort_mat(maxt)

    for row in range(rows - 1):
        for column in range(columns):
            if maxt[row][column] != 0:
                indicator = column
                break
        r = row + 1
        while r < rows:
            if maxt[r][indicator] == 0:
                r += 1
                continue
            else:
                k = - maxt[r][indicator] / maxt[row][indicator]
                func = lambda x, y: x + k * y
                maxt[r] = list(map(func, maxt[r], maxt[row]))
                r += 1
        maxt = sort_mat(maxt)

    return maxt



def flip(mat):
    rows = len(mat)
    columns = len(mat[0])
    new_mat = []

    for row in range(rows):
        for column in range(columns):
            new_mat.append(mat[row][column])
    new_mat.reverse()
    new_mat = create_matrix(rows, columns, new_mat)
    return new_mat
    

def reduced_echelon_form(mat):
    mat = echelon_form(mat)
    mat = flip(mat)
    mat = echelon_form(mat)
    mat = flip(mat)
    return mat


def main():
    matrix = create_matrix(4, 5, [0, 0, 0, 0, 1, 1, 2 , 3, 4, 5, 0, 0, 0, 2, 0, 3, 4, 5, 6, 7])
    matrix = echelon_form(matrix)
    matrix = flip(matrix)
    #matrix = echelon_form(matrix)
    #matrix = sort_mat(matrix)
    #matrix = reduced_echelon_form(matrix)
    display_matrix(matrix)
    #print(is_echelon_form(matrix))


main()
