from Algorithm28 import GenerateMove


def inthesamediagnal(cell1, cell2):
    if cell1 == cell2:
        return False

    pos1 = GenerateMove(cell1)
    pos2 = GenerateMove(cell2)

    x = abs(int(pos1[0]) - int(pos2[0]))
    y = abs(int(pos1[1]) - int(pos2[1]))

    if x == y:
        return True
    else:
        return False

def ReturnPos(cell):
    new_cell = cell
    dict_pos = {
        '1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h'
    }
    numpos = '12345678'
    if cell[0] in numpos:
        new_cell = dict_pos.get(cell[0]) + cell[1]
    return new_cell


def positioninadiagnal(cell1, cell2):
    pos1 = GenerateMove(cell1)
    pos2 = GenerateMove(cell2)
    pos = []
    list_of_pos = []
    x1 = int(pos1[0]) - 1
    x2 = int(pos2[0]) - 1
    y1 = int(pos1[1]) - 1
    y2 = int(pos2[1]) - 1

    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1

    for x in range(0, 8):
        y = int(a)*x + int(b)
        if 0 <= y <= 7:
            pos.append(x + 1)
            pos.append(y + 1)
            list_of_pos.append(pos)
            pos = []
    return list_of_pos


def bishopDiagonal(bishop1, bishop2):
    new_pos1 = ''
    new_pos2 = ''
    final_pos = []

    if not inthesamediagnal(bishop1, bishop2) :
        final_pos.append(bishop1)
        final_pos.append(bishop2)
        final_pos.sort()
        return final_pos
    else:
        list_of_pos = positioninadiagnal(bishop1, bishop2)
        bishop1 = GenerateMove(bishop1)
        bishop2 = GenerateMove(bishop2)

        x = abs(int(bishop1[0]) - list_of_pos[0][0])
        y = abs(int(bishop2[1]) - list_of_pos[0][0])
        z = len(list_of_pos)
        if x < y:
            new_pos1 = str(list_of_pos[0][0]) + str(list_of_pos[0][1])
            new_pos2 = str(list_of_pos[z-1][0]) + str(list_of_pos[z-1][1])
            new_pos1 = ReturnPos(new_pos1)
            new_pos2 = ReturnPos(new_pos2)
            final_pos.append(new_pos1)
            final_pos.append(new_pos2)
        else:
            new_pos2 = str(list_of_pos[0][0]) + str(list_of_pos[0][1])
            new_pos1 = str(list_of_pos[z - 1][0]) + str(list_of_pos[z - 1][1])
            new_pos1 = ReturnPos(new_pos1)
            new_pos2 = ReturnPos(new_pos2)
            final_pos.append(new_pos1)
            final_pos.append(new_pos2)
        final_pos.sort()
        return final_pos




#print(inthesamediagnal("d8", "b5"))
#print(bishopDiagonal("b3", "c2"))
#print(GenerateMove(''))
#print(positioninadiagnal('d7', 'f5'))
#print(ReturnPos('a1'))