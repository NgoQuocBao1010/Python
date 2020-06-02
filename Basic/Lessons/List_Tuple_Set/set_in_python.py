'''
Set tương tự như list, chuỗi, hay tuple
Có thể lưu trữ được các dữ liệu ngoại trừ các dữ liệu unhashable như list hay chính nó
Set khong giữ các giá trị trùng nhau mà chỉ lấu
1 empty set khong phai la set tru khi ep du lieu
'''




set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
print(set1)

set1 = {1,1,3,4,6,7,7,8}
print(set1) # khong luu cac gia tri cung nhau

set1 = {i*2 for i in range(0,5) }
print(set1)

set1 = (1, 'Bao', 8.5)
print(type(set(set1)), '\n') #ep du lieu cho set

# cac ham

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
print(8 in set1) #tra ve TRUE hay FALSE
print(set1 - {'Xin Chao', 8.5}) #Tra ve 1 set moi giong nhu set1 bo cac phan tu
print(set1 & {(1,2,3), 'Bao', 8.5}) #Tra ve 1 set moi chua cac phan tu giao giua 2 set
print(set1 | {5,('Chelsea', 3.5)}) # tra ve 1 set moi co cac phan tu cua ca 2 set
print(set1 ^ {8, 8.5, 'Bao', 3}) # Tra ve 1 set moi bao gom 2 set cu cong lai nhung bo cac phan tu trung nhau


set1.clear() #xoa cac phan tu trong set
print(set1, '\n')

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
hamPop = set1.pop() #lay ra phan tu dau tien

print(hamPop)
print(set1, '\n')

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
set1.remove(8) # loai bo 1 phan tu co trong set (khong co se bao loi)
print(set1, '\n')

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
set1.discard(8)
print(set1)
set1.discard(80) # giong nhu remove nhung khong co thi khong bao loi
print(set1, '\n')

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
set2 = set1.copy() #tao ra ban sao cua set 1
print(set2, '\n\n\n')




# Bai tap
# khong duoc gán 2 set vao nhau
set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
set2 = set1.copy()

set2.clear()
print(set1)
print(set2, '\n\n\n')

set1 = {'Xin Chao', 8, 8.5, (1,2,3)}
set2 = set1 # khi gán 2 set thì cả 2 set2 vá set 1 sẽ cùng trỏ về 1 chỗ nên thay đổi a thì b cũng sẽ thay đổi

set2.clear()
print(set1)
print(set2)