
# for cơ bản

list1 = [x + 3 for x in range(10)]
for x in list1:
	print('->', x)
	
print('\n')


player = {'name': 'Pulisic', 'age': 18}

for chiakhoa, giatri in player.items():
	print(chiakhoa, '=>', giatri)

print('\n')
# break và continue, else sử dụng giống 




player = {'name': 'Pulisic', 'age': 18}

for chiakhoa, giatri in player.items():
	if chiakhoa == 'age':
		break
	print(chiakhoa, '=>', giatri)

print('#\n')



player = {'name': 'Pulisic', 'age': 18}

for chiakhoa, giatri in player.items():
	if chiakhoa == 'name':
		continue
	print(chiakhoa, '=>', giatri)

print('\n')


# bài 2

set_ = {5, 8, 1, 9, 4}
sum = 0
for i in set_:
	sum += i;

print(sum)











