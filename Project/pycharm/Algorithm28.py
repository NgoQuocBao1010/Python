def GenerateMove(cell):
    new_cell = cell
    moves_dict = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8'
    }
    char_lst = 'ABCDEFGH'
    if cell[0].upper() in char_lst:
        new_cell = moves_dict.get(cell[0].upper()) + cell[1]
    return new_cell




#print(GenerateMove('a1'))
#print(bishopAndPawn("e7", "d6"))



