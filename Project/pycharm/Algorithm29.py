from Algorithm28 import GenerateMove

def chessKnight(cell):
    Knight_pos = GenerateMove(cell)
    possible_move = 8

    if Knight_pos[0] == '2' or Knight_pos[0] == '7':
        if Knight_pos[1] == '2' or Knight_pos[1] == '7':
            possible_move -= 4
        elif Knight_pos[1] == '1' or Knight_pos[1] == '8':
            possible_move -= 5
        else:
            possible_move -= 2

    elif Knight_pos[0] == '1' or Knight_pos[0] == '8':
        if Knight_pos[1] == '2' or Knight_pos[1] == '7':
            possible_move -= 5
        elif Knight_pos[1] == '1' or Knight_pos[1] == '8':
            possible_move -= 6
        else:
            possible_move -= 4

    else:
        if Knight_pos[1] == '2' or Knight_pos[1] == '7':
            possible_move -= 2
        elif Knight_pos[1] == '1' or Knight_pos[1] == '8':
            possible_move -= 4

    return possible_move

print(chessKnight("a3"))
