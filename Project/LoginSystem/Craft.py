from Database import convert_to_list
from collections import Counter


'''
def is_winner():
	index = 0
	if board[index] != '-' and board[index] == board[index + 1] and board[index] == board[index + 2]:
		return True

	if board[index] != '-' and board[index] == board[index + 3] and board[index] == board[index + 6]:
		return True

	if board[index] != '-' and board[index] == board[index + 4] and board[index] == board[index + 8]:
		return True

	index = 1
	if board[index] != '-' and board[index] == board[index + 3] and board[index] == board[index + 6]:
		return True

	index = 3
	if board[index] != '-' and board[index] == board[index + 1] and board[index] == board[index + 2]:
		return True

	index = 2
	if board[index] != '-' and board[index] == board[index + 2] and board[index] == board[index + 4]:
		return True

	return False

'''
import random
lst = [1, 2, 5]
print(random.choice(lst))
lst1 = Counter([1, 2])
#lst2 = lst1&lst


#print(list(lst2.elements()))