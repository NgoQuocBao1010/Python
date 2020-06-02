rows = 6
columns = 8
dungeon = [['.', '##', '##', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '~~', '~~', '.', '##'], ['.', '##', '.', '.', '.', '##', '.', 'End'], ['.', '.', '##', '.', '##', '.', '.', '.'], ['.', '##', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '##', '.', '##', '.', '.']]


# Visualize dungeon
def visualizeDungeon(dungeon):
	for row in range(rows):
		result = '** '
		for column in range(columns):
			result += str(dungeon[row][column]) + '\t\t'
		result += '**'
		print(result)



# Necessary variables

# starting position
start = (0, 0)
start_row, start_col = start

# ending position
end = (2, 7)

# queue to store position while finding path
from collections import deque
row_queue = deque()
col_queue = deque()

# array to check if place is visited
visited = [[False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False]]

# array to re-create the path
prev = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]

# Variables to keep track of the steps
move_count = 0 # count the minimum steps
nodes_left_in_layer = 1
nodes_in_next_layer = 0


reached_end = False # check if the end is reached


def getNeighbours(row, col):
	global nodes_in_next_layer
	direction_rows = [0, 0, -1, 1]
	direction_cols = [1, -1, 0, 0]

	for direction in range(4):
		new_row = row + direction_rows[direction]
		new_col = col + direction_cols[direction]

		if new_col < 0 or new_row < 0:
			continue
		if new_col >= columns or new_row >= rows:
			continue

		if visited[new_row][new_col]:
			continue

		if dungeon[new_row][new_col] == '##' or dungeon[new_row][new_col] == '~~':
			 continue


		row_queue.append(new_row)
		col_queue.append(new_col)
		visited[new_row][new_col] = True
		prev[new_row][new_col] = (row, col)
		nodes_in_next_layer += 1


def recounstructPath(start, end, prev):

	path = []
	at = end

	while at is not None:
		path.append(at)
		at = prev[at[0]][at[1]]

	path.reverse()

	if path[0] == start:
		return path
	return []


def findShortestPath():
	global reached_end, move_count, nodes_left_in_layer, nodes_in_next_layer, start, end, prev
	row_queue.append(start_row)
	col_queue.append(start_col)
	visited[start_row][start_col] = True

	while len(row_queue) > 0: # or len(col_queue) > 0:
		row = row_queue.popleft()
		col = col_queue.popleft()

		if dungeon[row][col] == 'End':
			reached_end = True
			break

		getNeighbours(row, col)
		nodes_left_in_layer -= 1

		if nodes_left_in_layer == 0:
			nodes_left_in_layer = nodes_in_next_layer
			nodes_in_next_layer = 0
			move_count += 1

	print(prev)
	path = recounstructPath(start, end, prev)

	if reached_end:
		return (move_count, path)
	return -1





# visualizeDungeon(dungeon)
print(findShortestPath())

