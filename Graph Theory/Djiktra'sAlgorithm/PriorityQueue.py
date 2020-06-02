class KeyValuePair:
	def __init__(self, keyvalue=(0, 0)):
		self.key, self.value = keyvalue


	def __eq__(self, other):
		return self.value == other.value


	def __ne__(self, other):
		return self.value != other.value


	def __lt__(self, other):
		return self.value < other.value


	def __le__(self, other):
		return self.value <= other.value


	def __gt__(self, other):
		return self.value > other.value


	def __ge__(self, other):
		return self.value >= other.value


	def __hash__(self):
		return id(self)


	def __str__(self):
		return f'{self.key}: {self.value}'


class PriorityQueue:
	heapSize 			= 0 	# number of element inside priority queue (PQ) (also the heap)
	heapCapacity		= 0		# the size of the list that contains element (may bigger than the heapsize)

	heap 				= []	# List to track elements in side the heap

	mapIndex 			= {}   	# map to keep track of indeces of a particular element in the heap

	def __init__(self, elements=[]):

		for element in elements:
			self.add(element)

	# Return the length of the priority queue
	def __len__(self):
		return self.heapSize

	# clear everything in the heap
	def clear(self):
		for index in range(self.heapCapacity):
			self.heap[index] = None

		self.heapSize = 0
		self.mapIndex.clear()


	# return the first element of PQ if it is not empty, otherwise return None
	def peek(self):
		if len(self) == 0:
			return None
		return self.heap[0]


	# pull out and return the first element of PQ
	def poll(self):
		if len(self) == 0:
			return None
		return self.removeAt(0)

	# Test if element is in the PQ
	def contains(self, element):
		if element is None:
			return False

		return element in self.mapIndex


	def add(self, keyvalue=(0, 0)):
		if keyvalue is None:
			raise IlligalArgumentException

		element = KeyValuePair(keyvalue)
		if self.heapSize < self.heapCapacity:
			self.heap[self.heapSize] = element

		else:
			self.heap.append(element)
			self.heapCapacity += 1


		self.mapAdd(element, self.heapSize)

		self.swim(self.heapSize)
		self.heapSize += 1


	# Test if node i <= node j
	def less(self, i, j):
		node1 = self.heap[i]
		node2 = self.heap[j]

		return node1 <= node2


	# Bottom up a node in a heap
	def swim(self, position):

		parentPos = (position - 1) // 2 # get the index of parent node

		while position > 0 and self.less(position, parentPos):

			self.swap(parentPos, position)
			position = parentPos

			parentPos = (position - 1) // 2


	# Top down a node in a heap
	def sink(self, position):
		while True:
			left 			= 2 * position + 1
			right			= 2 * position + 2
			smallest 		= left


			if right < self.heapSize and self.less(right, left):
				smallest 	= right


			if left >= self.heapSize or self.less(position, smallest):
				break

			self.swap(smallest, position)
			position = smallest


	# swap 2 nodes' positions
	def swap(self, pos1=0, pos2=0):

		node1 = self.heap[pos1]
		node2 = self.heap[pos2]

		self.heap[pos1] = node2
		self.heap[pos2] = node1

		self.mapSwap(node1, node2, pos1, pos2)


	# remove an element in a PQ
	def remove(self, element):
		if element is None:
			return False


		index = self.mapIndex.get(element)

		if index is not None:
			self.removeAt(index)
		return index is not None


	# remove a node by its given index
	def removeAt(self, index):
		if len(self) == 0:
			return None

		self.heapSize -= 1
		removeData = self.heap[index]

		self.swap(index, self.heapSize)

		self.heap[self.heapSize] = None
		self.mapRemove(removeData, self.heapSize)

		if index == self.heapSize:
			return (removeData.key, removeData.value)


		element = self.heap[index]

		self.sink(index)

		if self.heap[index] == element:
			self.swim(index)

		return (removeData.key, removeData.value)


	
	# Check if the node is satitfies MinHeap conditions
	def isMinHeap(self, position):
		if position >= self.heapSize:
			return True


		left = 2 * position + 1
		right = 2 * position + 2

		if left < self.heapSize and not self.less(position, left):
			return False

		if right < self.heapSize and not self.less(position, right):
			return False


		return self.isMinHeap(left) and self.isMinHeap(right)


	# add element to the mapIndex
	def mapAdd(self, value, index):
		self.mapIndex.setdefault(value, index)


	# Remove element from the mapIndex
	def mapRemove(self, value, index):
		self.mapIndex.pop(value)


	# swap 2 elements in the map
	def mapSwap(self, val1, val2, valIndex1, valIndex2):
		self.mapIndex[val1] = valIndex2
		self.mapIndex[val2] = valIndex1


	def __str__(self):
		result = '***\n'

		for element in self.heap:
			result += '\t\t' + str(element) + '\n'

		result += '\n\t\t\t\t\t\t\t\t\t\t***'
	
		return result
	

# A = KeyValuePair(('A', 5))
# B = KeyValuePair(('B', 2))
# C = KeyValuePair(('C', 2))

# PQ = PriorityQueue()
# PQ.add((5, 0))
# PQ.add((6, 1))
# PQ.add((1, 3))
# PQ.add((2, 2))
# # # print(PQ)
# th = PQ.poll()
# # th = PQ.poll()
# # th = PQ.poll()
# # th = PQ.poll()
# print(th)