board = ['-' for x in range(9)]
temp_board = ['X', '-', 'O', 'O', 'O', 'X', 'X', '-', 'O']


def print_board(bd):
	print(bd[0] + " || " + bd[1] + " || " + bd[2])
	print('===========')
	print(bd[3] + " || " + bd[4] + " || " + bd[5])
	print('===========')
	print(bd[6] + " || " + bd[7] + " || " + bd[8])


def insert_board(player, pos, bd):
	if player == 'user':
		bd[pos] = 'X'
	else:
		bd[pos] = 'O'


def player_move(bd):
	pos = input('Enter a location (1-9): ')

	try:
		pos = int(pos) - 1

		if pos < 0 or pos > 8:
			print('Please enter number in the range!')
			return False
		elif not is_free(pos, bd):
			print('This location is occupied!!')
			return False
		else:
			insert_board('user', pos, bd)
			return True
	except:
		print('Please enter a number!!')
		return False


def is_free(pos, bd):
	return bd[pos] == '-'


def is_full(bd):
	return bd.count('-') == 0


def is_won(bd):
	winner_brackets = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
					  [1, 4, 7], [2, 5, 8], [3, 6, 9],
					  [1, 5, 9], [3, 5, 7]]

	for bk in winner_brackets:
		if bd[bk[0]-1] != '-':
			if bd[bk[0] - 1] == bd[bk[1] - 1] and bd[bk[0] - 1] == bd[bk[2] - 1]:
				return True

	return False


def comp_move(bd):
	possible_moves = [pos for pos, letter in enumerate(bd) if letter == '-']

	for player in ['c', 'user']:
		for pos in possible_moves:
			clone_bd = bd[:]
			insert_board(player, pos, clone_bd)
			if is_won(clone_bd):
				insert_board('c', pos, bd)
				return

	possible_corner_moves = []
	for pos in [0, 2, 6, 8]:
		if bd[pos] == '-':
			possible_corner_moves.append(pos)
	if len(possible_corner_moves) > 0:
		import random
		pos = random.choice(possible_corner_moves)
		insert_board('c', pos, bd)
		return

	possible_edge_moves = []
	for pos in [1, 3, 5, 7]:
		if bd[pos] == '-':
			possible_edge_moves.append(pos)
	if len(possible_edge_moves) > 0:
		import random
		pos = random.choice(possible_edge_moves)
		insert_board('c', pos, bd)
		return


def main():
	print_board(board)
	run = True

	while run:
		if not is_full(board):
			make_move1 = player_move(board)
			while not make_move1:
				player_move(board)
			if is_won(board):
				print_board(board)
				print('You won')
				break

			comp_move(board)
			print_board(board)
			if is_won(board):
				print('Sorry')
				run = False
		else:
			print_board(board)
			print('Tie game!!')
			run = False


main()
#print_board(temp_board)
#print('\n')
#comp_move(temp_board)
#print_board(temp_board)

