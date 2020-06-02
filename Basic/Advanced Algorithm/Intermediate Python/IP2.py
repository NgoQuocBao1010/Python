#1. SỬ DỤNG DICTIONARY THAY CHO IF ELSE:

def do_math(x1, operator, x2):
	if operator == 'x':
		return x1 * x2
	elif operator == '/':
		return x1 / x2
	elif operator == '+':
		return x1 + x2
	elif operator == '-':
		return x1 - x2

def do_math2(x1, operator, x2):
	return {
		'x': lambda : x1 * x2,
		'/': lambda : x1 / x2,
		'+': lambda : x1 + x2,
		'-': lambda : x1 - x2
	}.get(operator, lambda : None)()

def main():
	while True:
		print('\t\tAdvanced Python\n')
		print('\tPress 1. Using dictionary as Switch Case')
		print('\tPress 0. Exit')
		op = int(input('Enter your option: '))

		if op == 1:
			x1 = int(input('Enter your first number: '))
			x2 = int(input('Enter your second number: '))
			operator = input('What do you want to do?: ')
			print('The do_math and do_math2 function perform exactly the same\nBut the do_math2 using dictionary to simplify the code')
			print('do_math func: ' ,do_math(x1, operator, x2))
			print('do_math2 func: ' ,do_math(x1, operator, x2))
		else:
			break


#main()