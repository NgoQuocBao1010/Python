def check_valid_string(string):
	operand = '+-x/^%'
	time_divide = 'x/'
	num = '0123456789'
	bracket = '()'
	stack = []

	if len(string) == 0:
		return False

	for letter in string:
		if letter not in operand and letter not in num and letter not in bracket:
			return False

	if string[len(string) - 1] in operand:
		return False

	for index in range(len(string)-1):
		if string[index] in time_divide and string[index+1] in time_divide:
			return False

	for element in string:
		if element == '(':
			stack.append(element)
		elif element == ')':
			if len(stack) == '0':
				return False
			else:
				stack.pop()
	if len(stack) > 0:
		return False
	else:
		return True
	return True


def convert_string(string):
	ignore = '0123456789()'
	plus_minus = '+-'
	stack = []
	new_string = ''

	for index in range(len(string)):
		if string[index] in ignore:
			if len(stack) > 0:
				a = stack.count('-')
				if a % 2 == 0:
					new_string += '+'
				else:
					new_string += '-'
				stack.clear()
			new_string += string[index]
		else:
			if string[index] not in plus_minus:
				new_string += string[index]
			else:
				stack.append(string[index])
	return new_string


def convert_to_list(string):
	lst = []
	var = ''

	string = convert_string(string)
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
	return lst


def priority(symbol):
	if symbol == '(':
		return -1 
	elif symbol == '+' or symbol == '-':
		return 0
	elif symbol == 'x' or symbol == '/':
		return 1
	elif symbol == '^' or symbol == '%':
		return 2


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
		return x1 / x2
	elif symbol == '^':
		return x1 ** x2
	elif symbol == '%':
		return x1 % x2
	elif symbol == None:
		return x1


def calculate(string):
	stack = []
	operand = '+-x/^%'

	if not check_valid_string(string):
		return '**Error 404**'

	postfix = transform_to_postfix(convert_to_list(string))
	for element in postfix:
		if str(element) not in operand:
			stack.append(element)
		else:
			x1 = stack.pop()
			x2 = stack.pop()
			result = do_operator(x2, element, x1)
			stack.append(result)

	return stack[0]

print(convert_string('3+(-8--4)x5'))
#print(check_valid_string('6-(5)'))
#print(convert_to_list('3-(9+9)'))
#print(transform_to_postfix(convert_to_list('5-(4+5)-7')))
#print(calculate('5-(4+5)-7'))

