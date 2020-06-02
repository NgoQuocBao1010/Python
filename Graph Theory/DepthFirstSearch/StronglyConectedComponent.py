# Preresent Graph

graph = {
	0: [],
	1: [7, 13],
	2: [11, 14, 15],
	3: [14, 15],
	4: [5, 9],
	5: [4, 6],
	6: [5, 9],
	7: [1, 13],
	8: [],
	9: [4, 6],
	10: [12],
	11: [2, 15],
	12: [10],
	13: [1, 7],
	14: [2, 3],
	15: [2, 3, 11],
}


size = 16 # size of graph
count = 0

components 			= [None] * size # array to keep label component
visited 	 		= [False] * size # array to check if node is visted


def getNeighbour(node_at):
	# print(node_at, graph.get(node_at))
	return graph.get(node_at)


def dfs(node_at):
	visited[node_at] = True
	components[node_at] = count

	for neighbour in getNeighbour(node_at):
		if not visited[neighbour]:
			dfs(neighbour)


def findComponents():
	global count

	for node in range(size):
		if not visited[node]:
			count += 1
			dfs(node)

	return (count, components)


number_of_components = findComponents()[1]
print(number_of_components)