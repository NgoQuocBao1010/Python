import random

for each_time in range(3):
    print(random.random())

print('\n\n')

for each_time in range(3):
    print(random.randint(10, 20))

print('\n\n')

name = ['Chelsea', 'Man City', 'Liverpool', 'Man Utd']

print(f'The best team is {random.choice(name)}')
