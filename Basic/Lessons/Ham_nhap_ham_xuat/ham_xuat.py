# nếu sử dụng hàm print mặc định thì python sẽ tự thêm vào khoanagr trắng giữa các dữ liệu
print("Default")
print('Bao', 'Xin Chao', 'Chelsea', '\n')

# thêm adaptor set vào để chỉnh
print('Seperate: ')
print('Bao', 'Xin Chao', 'Chelsea', sep= '***') # thay vì cách nhau bằng dấu ' ' thì sẽ cách bằng '***'
print('Bao', 'Xin Chao', 'Chelsea', sep= '...')
print('\n\n')



# nếu sử dụng hàm print nhiều lần mặc định thì python sẽ tự xuống hàng  
print("Default")
print(1)
print(2, '\n')


print('End: ')
print(1, end=';;;') # đổi \n thành ;;;
print(2)
print('\n')

# hàm 'đợi'
print('hàm đợi: ')
from time import sleep # nhập hàm sleep từ thư viện time

print('Quốc', end=' ')
sleep(1) # dừng chương trình 1s
print('Bảo')

print('\n')


'''Hàm dưới sẽ tự tạo 1 file tên hamxuat.txt 
	và ghi ok babe vào'''

'''with open('hamxuat1.txt', 'w') as fle:
	print('OK babe', file=fle)'''




from time import sleep

line = 'My idol is Cristiano Ronaldo'
 
for c in line:
	print(c, end='')
	sleep(0.1)


