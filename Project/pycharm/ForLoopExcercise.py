numbers = [5, 2, 5, 2, 2]
letter = 'x'
# first solution:
for value in numbers:
    for print_letter in range(value):
        print(letter, end='')
    print('')

print('\n\n')


#second solution:
for x_count in numbers:
    print('x' * x_count)