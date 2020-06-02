''' Lambda bản chất là 1 function nhưng ngắn gọn hơn so với def
	Do đó khỏi phải đặt tên cho lambda
	lambda cũng có hàm default như def
	Trong Lamda chỉ có 1 câu lệnh duy nhất'''


average = lambda a, b, c = -3: (a + b + c)/3

print(average(1, 2 ,3)) # truyền ba số vào và tính tb cộng
print(average(0, 8)) # truyền 2 số thì sẽ lấy default c = -3
print('\n')

# sử dụng cho list

lst = [lambda x: x**2, lambda x: x - 4, lambda x: x % 5]

for value in lst:
	print(value(5), end=' ')

print('\n\n')


# if else cho lambda

number_divided_4_and_5 = lambda x: ('Divided for both' if x % 5 == 0 else 'Not this number') if x % 4 == 0 else 'Not this number'

print(number_divided_4_and_5(81))
print('\n\n')

number_divided_4_and_5_part_2 = lambda x: 'Divided for both' if (x % 5 == 0 and x % 4 == 0) else 'Not this number'
print(number_divided_4_and_5_part_2(41))




