it = (x  for x in range(10)) # cách tạo 1 iterator
print(it) # không thể lấy iterator 1 cách trực tiếp
print(next(it)) # dùng hàm next để truy xuất từng phần tử của iterator
print(next(it))
print(next(it)) # nếu truy xuất quá số lượng phần tử thì sẽ lỗi

print("Hàm Sum :",sum(it), '\n\n') # tính tổng rồi đưa con trỏ về cuối 
#print("Hàm Sum nhưng thêm 1 số phía sau:",sum(it, 34)) #không thể chạy được vì đã sum ở trên rồi, bằng sum ở trên + với số thêm vào


it = [7, 8, 9 , 10]

print("Ham Max:",max(it)) #kiếm giá trị lớn nhất trong 1 list đưa vào
print(max(1,2,3,4,5,6,7)) # cách khác để dùng max
print(max([], default= 'Khong tim thay'), '\n\n') # không tìm thấy giá trị lớn nhất sẽ trả về default



it = (7, 15, 7.3, 32, 1)

print('Hàm Sorted: ',sorted(it)) # mặc định sẽ sắp từ bé đến lớn
print(sorted(it, reverse= True)) # thêm reverse sẽ sắp xếp ngược lại














