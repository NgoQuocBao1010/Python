# while cơ bản

tuoi = 15
while tuoi <= 18:
	print('Ban chỉ mới ', tuoi, 'tuổi. Chưa đủ tuổi coi phim này')
	tuoi += 1

print('\n')


a = 'My idol is Cristiano Ronaldo'

vi_tri = 0

while vi_tri < len(a) :
	print('Chu thu ', vi_tri + 1, 'la', a[vi_tri])
	vi_tri += 1

print('\n')


Five_numbers_that_is_divided_by_3 = []
so = 1


while True: # vòng lặp sẽ chạy mãi mãi nếu không có hàm break
	if so % 3 == 0:
		Five_numbers_that_is_divided_by_3.append(so)
		if len(Five_numbers_that_is_divided_by_3) == 5:
			break;
	so += 1;		


print(Five_numbers_that_is_divided_by_3)
print(so)
print('\n')


# dùng continue để quay lại vòng lặp và bơ mấy thứ ở dưới
x = 0
while x < 18:
	x += 1
	if x % 4 != 0:
		continue # nếu x không chia hết cho 4 thì sẽ bơ câu lệnh print và quay lên vòng lặp
	print(x, 'chia het cho 4')


print('\n')


# câu lệnh else chạy sau khi câu lệnh while kết thúc
x = -5

while x < 0:
	print(x, 'is a negative number')
	x += 1
else:
	print('x is no longer a negative number')


print('\n')
# nếu có câu lệnh break thì else sẽ không chạy

x = -5

while x < 0:
	print(x, 'is a negative number')
	x += 1
	if x == -1:
		break
else:
	print('x is no longer a negative number')
print('\n')


it = (x for x in range(5)) # danh sách là 0, 1, 2, 3, 4

while True: #đây là điều kiện luôn đúng nên chương trình có thể chạy mãi mãi
	try: # in phần tử kế tiếp chừng nào gặp lỗi St... thì break;
		print(next(it))
	except StopIteration:
		break	








#Bài tập

# 1:

Five_numbers_that_is_divided_by_3 = []
so = 0

while len(Five_numbers_that_is_divided_by_3) <= 5:
	so += 1
	if(so % 3 != 0):
		continue
	Five_numbers_that_is_divided_by_3.append(so)


print(Five_numbers_that_is_divided_by_3,'\n\n')


#3 sắp xếp lại mảng nhưng giữ các vị trí 11

arr = [56, 14, 11, 576, 34, 90, 11, 11, 65, 0, 11, 35]
print(arr)
vt = 0;
temp = 0
while vt < len(arr):
	if (arr[vt] != 11):
		vt2 = vt + 1
		while vt2 < len(arr):
			if arr[vt] > arr[vt2] & arr[vt2] != 11:
				temp = arr[vt]
				arr[vt] = arr[vt2]
				arr[vt2] = temp
			vt2 += 1
	vt += 1



print(arr, '\n\n')



# bài tập 2 

with open('file1.txt') as fle:
	list_file = fle.readlines()

#print(list_file)

vtphantulist = 0

while vtphantulist < len(list_file):
	list_oneline = list_file[0].split()
	vtphantuline = 0
	while vtphantuline < len(list_oneline):
		if list_oneline[vtphantuline] == 'Kteam':
			list_oneline[vtphantuline - 1] = 'How'
		vtphantuline += 1
	new_line = ''
	new_line += ' '.join(list_oneline) + '\n'
	vtphantulist += 1

	with open('kteam.txt', mode= 'w') as new_fle:
		new_fle.write(new_line)





















