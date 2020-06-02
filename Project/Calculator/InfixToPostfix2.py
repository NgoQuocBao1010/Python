def priority(symbol):
	if symbol == '(':
		return -1 
	elif symbol == '+' or symbol == '-':
		return 0
	elif symbol == 'x' or symbol == '/':
		return 1
	elif symbol == '^' or symbol == '%':
		return 2


def is_a_number(a):
	a = str(a)
	for index in range(len(a)):
		if '0' <= a[index] <= '9':
			return True

	return False


def renew_string(sr):
	new_sr = ''
	stack = []
	plus_minus = '+-'

	for index in range(len(sr)):
		if sr[index] not in plus_minus:
			if len(stack) == 0:
				new_sr += sr[index]
			else:
				a = stack.count('-')
				if a % 2 == 0:
					new_sr += '+'
				else:
					new_sr += '-'
				new_sr += sr[index]
			stack.clear()
		else:
			stack.append(sr[index])
	
	return new_sr


def check_for_bracket(lst):
	for element in lst:
		if str(element) in '()':
			return True
	return False


def convert_to_list(string):
	lst = []
	var = ''
	string = renew_string(string)
	operand = '+-x/^%'

	for element in string:
		if '0' <= element <= '9':
			var += element
		else:
			if var != '':
				lst.append(int(var))
			lst.append(element)
			var = ''
	if var != '':
		lst.append(int(var))

	if check_for_bracket(lst):
		if lst[0] != '(':
			for index in range(1, len(lst)):
				if lst[index] == '(' and lst[index - 1] == '-':
					lst[index - 1] = '+'
					index2 = index + 1

					while lst[index2] != ')':
						if str(lst[index2]) in 'x/':
							index2 += 2
							continue
						if is_a_number(lst[index2]) :
							lst[index2] = -lst[index2]
						index2 += 1
				elif lst[index] == '(' and lst[index - 1] != '-':
					break
	
	return lst


def renew_list(lst):
	bracket = '()'
	operand = '+-x/^%'
	infix = []

	for index in range(len(lst) - 1):
		if lst[index] == '-' and is_a_number(lst[index+1]):
			lst[index] = '+'
			lst[index+1] = -lst[index+1]

	if str(lst[0]) not in operand:
		infix.append(lst[0])

	plus_minus = '+-'
	for index in range(1, len(lst)):
		if str(lst[index]) in plus_minus and is_a_number(lst[index-1]) :
			infix.append(lst[index])
			continue
		elif str(lst[index]) not in plus_minus:
			infix.append(lst[index])

	return infix



def transform_to_postfix(lst):
	postfix = []
	operand = '+-x/^%()'	
	stack = []

	for index in range(len(lst)):
		if str(lst[index]) not in operand:
			postfix.append(lst[index])
		else:
			if lst[index] == ')':
				while True:
					sym = stack.pop()
					if sym == '(':
						break
					else:
						postfix.append(sym)
				continue
			if len(stack) == 0 or lst[index] == '(':
				stack.append(lst[index])
			else:
				top = stack[len(stack) - 1]

				if priority(lst[index]) > priority(top):
					stack.append(lst[index])
				else:
					while len(stack) > 0:
						sym = stack.pop()
						if sym != '(':
							postfix.append(sym)
					stack.append(lst[index])

	while len(stack) > 0:
		sym = stack.pop()
		if sym != '(':
			postfix.append(sym)

	return postfix


def do_operator(x1, symbol=None, x2=0):
	if symbol == '+':
		return x1 + x2
	elif symbol == 'x':
		return x1 * x2
	elif symbol == '-':
		return x1 - x2
	elif symbol == '/':
		try:
			return x1 / x2
		except ZeroDivisionError:
			return "Zero Divison Error"
	elif symbol == '^':
		return x1 ** x2
	elif symbol == '%':
		try:
			return x1 % x2
		except:
			return "Zero Divison Error"
	elif symbol == None:
		return x1


def calculate(string):
	stack = []
	operand = '+-x/^%'

	string = convert_to_list(string)
	postfix = transform_to_postfix(renew_list(string))
	for element in postfix:
		if str(element) not in operand:
			stack.append(element)
		else:
			try:
				x1 = stack.pop()
				x2 = stack.pop()
				result = do_operator(x2, element, x1)
				stack.append(result)
			except IndexError:
				return "Error 404"

	return stack[0]

#print(renew_string('6-----(5+-----3)x2'))
'''
lst =  renew_list(convert_to_list('3-(2-7)'))
for element in lst:
	print(element, end=' ')'''

#print(calculate('3-(2-7)'))
