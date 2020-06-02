fle = open('file.txt') # mở file 
print('hàm read')
data = fle.read() # đọc trong file và trả về kiểu dữ liệu chuỗi, nếu không để gì trong read thì sẽ đọc hết cả read và TRẢ CON TRỎ VỀ VỊ TRÍ CUỐI của File nên muốn đọc tiếp phải close file và đọc lại
fle.close()
print(data, '\n')


fle = open('file.txt') 
data = fle.read(2) # read (4) là đọc ra 2 phần tử trong File con trỏ sẽ dừng lại ở vị trí thứ 2
data2 = fle.read(4) # con trỏ sẽ bắt đầu từ vị trí thứ 2
fle.close()
print(data)
print(data2, '\n\n')


fle = open('file.txt')
data = fle.readline() # chỉ đọc trong 1 hàng nếu thêm số vào readline thì sẽ đọc ra số các ký tự trong hàng đó, con trỏ sẽ được đưa về cuối file
data2 = fle.readline()
fle.close()
print('hàm readline : ')
print(data)
print(data2, '\n')



fle = open('file.txt')
data = fle.readlines() # trả về 1 list trong đó mỗi phàn tử là 1 hàng
fle.close()
print("Ham readlines: ")
print(data, '\n\n')



# dùng để thêm vào file
'''fle = open('file.txt', mode = 'a+') # chế độ ghi vào file, hàm mode a+ này sẽ đưa con trỏ vào cuối file
data = fle.write('\nBao Quoc') # in cái này vào file
fle.close()'''



fle = open('file.txt')
data= fle.read() # con trỏ đã di chuyển về cuối file
data1 = fle.read() # nên hàm data 1 sẽ không đọc được gì trừ khi ta close file rồi mở lại
fle.seek(13) # hàm seek giúp ta đem con trỏ về vị trị ta muốn
data2 = fle.read() # bây giờ con trỏ sẽ đọc tiếp từ vị trí đó
fle.close()

print('Hàm seek: ')
print('data :',data)
print('data 1: \n',data1)
print('data 2:',data2)



# hàm with
''' hàm này sẽ tự đóng file sau khi thực hiện câu lệnh
	bởi vậy nên nếu sử dụng các câu lệnh tiếp theo sẽ không được vì file đã đóng
'''	
with open('file.txt') as fle:
    data = fle.read() # space 4 trước khi viết câu lệnh


print('Hàm read: ')
print(data, '\n\n')
'''
with open('file.txt', mode = 'a+') as fle:
	fle.write('\nCristiano Ronaldo')'''

# cách lấy dữ liệu bằng các hàm của iterator vì file là 1 iterator
fle = open('file.txt')
print(next(fle))
print(next(fle))
fle.close()

print('\n')










