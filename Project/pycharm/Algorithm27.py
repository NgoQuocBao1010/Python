def isWhite(cell):
    columnChar1 = ['A', 'C', 'E', 'G']
    columnChar2 = ['B', 'D', 'F', 'H']
    white = True

    if cell[0] in columnChar1:
        if int(cell[1]) % 2 == 0:
            white = True
        else:
            white = False
    else:
        if int(cell[1]) % 2 == 0:
            white = False
        else:
            white = True
    return white


def chessBoardCellColor(cell1, cell2):
    if isWhite(cell1) and isWhite(cell2):
        return True
    elif not isWhite(cell1) and not isWhite(cell2):
        return True
    else:
        return False

print(chessBoardCellColor('B3','H8'))
#print(isWhite('F5'))