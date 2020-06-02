# if cơ bản


b = -3

if b < 1:
	print('b nhỏ hơn 1', '\n')

a = 10;
if a < 1 :
	print('a nhỏ hơn 1')
elif a == 1:
	print('a bằng 1')
elif a > 1:
	print('a lớn hơn 1')
print('\n')

c = 100

if c < 0:
	print('c là số âm')
	print('Dễ vãi lồn')
else:
	print('c là số %d' %(c))
	print('Dễ vãi l**')
print('\n')


# các khai báo khác
a = 2
b = 3
if (a > b): print('a lớn hơn b'); a += 1; print(a)
else: print('a nhỏ hơn b'); b += 1; print(b)


# bài tập

a = 5
b = 9
c = 8

maximum = -100

if (a > maximum):
	maximum = a
if (b >= maximum):
	maximum = b
if( c >= maximum):
	maximum = c

print(maximum)






