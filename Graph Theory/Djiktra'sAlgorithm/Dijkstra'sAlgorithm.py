from PriorityQueue import PriorityQueue
import sys


class Edge:
	def __init__(self, node, distance):
		self.to 		= node
		self.distance 	= distance


	def __eq__(self, other):
		return self.distance == other.distance


	def __ne__(self, other):
		return self.distance != other.distance


	def __lt__(self, other):
		return self.distance < other.distance


	def __le__(self, other):
		return self.distance <= other.distance


	def __gt__(self, other):
		return self.distance > other.distance


	def __ge__(self, other):
		return self.distance >= other.distance


	def __hash__(self):
		return id(self)


	def __str__(self):
		return f'The distance to node {self.to} is {self.distance}'


MAX_INT = sys.maxsize # Variable preresents infinity

size = 5 # number of node

# list preresents the graph, list contains tuples (node, weight, node)
# for example (1, 2, 5): The weight from node 1 to node 2 cost 5 units
graph = {
	1: [Edge(2, 5), Edge(3, 2), Edge(4, 6)],
	2: [Edge(1, 5)],
	3: [Edge(1, 2), Edge(4, 1), Edge(5, 5)],
	4: [Edge(1, 6), Edge(3, 1)],
	5: [Edge(3, 5)]
}

start = 1 # starting node


# get the index of a node in a list
def getIndex(value):
	return {
		1: 0,
		2: 1,
		3: 2,
		4: 3,
		5: 4
	}.get(value)


def dijkstra(graph={}, size=0, start=0):
	start_index = getIndex(start)

	visited = [False] * size
	prev = [None] * size
	dist = [MAX_INT] * size
	dist[start_index] = 0

	pq = PriorityQueue()
	pq.add((start, 0))

	while len(pq) != 0:
		node, minDist = pq.poll()
		nodeIndex = getIndex(node)

		visited[nodeIndex] = True

		if dist[nodeIndex] < minDist:
			continue

		for edge in graph.get(node):
			edgeIndex = getIndex(edge.to)
			if visited[edgeIndex]:
				continue
			newDist = dist[nodeIndex] + edge.distance

			if newDist < dist[edgeIndex]:
				prev[edgeIndex] = nodeIndex
				dist[edgeIndex] = newDist
				pq.add((edge.to, newDist))

	return (dist, prev)


def findShortestPath(graph, size, start, end):
	dist, prev = dijkstra(graph, size, start)
	path = []

	if dist[end] == MAX_INT:
		return path

	at = end
	while at is not None:
		path.append(at)
		at = prev[at]

	path.reverse()
	return path


print(findShortestPath(graph, size, 1, 4))

	



