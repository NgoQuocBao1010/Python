a = range(61, 100, 3) # bắt đầu từ, kết thúc, bước nhảy

print(type(a))
print(a[3])
print(list(a))
print(73 in a)
print('\n')



lis_t = [5, 6.3, ['Bao', 1], ('chao', 100)]

for i in range(len(lis_t)):
	print(lis_t[i], end=' ')
print('\n')
'''
i = 0 
while i < len(lis_t):
	print(lis_t[i])
	i += 1
'''


# hàm emurate dùng để thêm số thứ tự vào các phần tử trong 1 list

player_list = ['Odoi', 'Pulisic', 'Loftus-Cheek', 'Mason Mount']


print('Hàm enumerate: ', end=' ')
print(enumerate(player_list), end=' ')
print('Kiểu dữ liệu :',type(enumerate(player_list)))

print(list(enumerate(player_list))) # để xuất ra cần ép cho nó kiểu tuple hay list





# bài tập 1

lst = [[1,2,3], [4,5,6]]

for i in range(len(lst)):
	for j in range(len(lst[i])):
		lst[i][0] = None

print(lst)

print('\n')
# bai 2
lst = [[0, 1, 2, 3, 4], [15, 16, 17, 18, 5], [14, 23, 24, 19, 6,], [13, 22, 21, 20, 7], [12, 11, 10, 9, 8]]

for row in range(len(lst)):
	for column in range( len(lst[row]) ):
		print(lst[row][column], end  =' ')
		if ( column == len(lst[row]) - 1):
			print("\n")

print('\n')

print('Ma tran da sua doi: ')
for row in range(len(lst)):
	for column in range( len(lst[row]) ):
		if lst[row][column] < 10:
			print("%02d" %(lst[row][column]), end = ' ')
		else:
			print(lst[row][column], end  =' ')
		if column == len(lst[row]) - 1:
			print("\n")
