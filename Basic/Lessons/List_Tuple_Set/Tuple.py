'''
tuple dược giới hạn bởi cặp ngoặc ()
Các phần tử tuple được phân cách bởi dấu ,
tuple có khả năng chứa mọi giá trị
Tốc độ truy xuất nhanh hơn list
Không thể thay đổi phần tử trong Tuple(giống chuỗi)

bảo vệ dữ liệu không bị thay đổi 
có thể dùng làm key của dictionary'''

tup = (3, 7.8, ['Quoc', 'Bao'], ('tuple', 'list'))
# hoặc tup = 3, 7.8, ['Quoc', 'Bao'], ('tuple', 'list') #không cần ngoặc
print(tup[2][0]) # lấy 1 phần tử trong tuple
print(type(tup),'\n')


#muốn sử dụng hàm i range như trong list thì phải CÓNSTRUCTOR

tup1 = (i for i in range(14)) # tạo 1 tuple từ 0 đến phần tử 14
a = tuple(tup1) #constructor tuple
print(tup1)
print(a,'\n')

tup2 = (i for i in range(1,40) if i % 3 == 0) # tạo 1 tuple từ 1 tới 40 với các phần tử chia hết cho 3
a = tuple(tup2)
print(a, '\n')


''' có thể cộng tuple với tuple
	không thể nhân các tuple với nhau nhưng có thể nhân tuple với các số nguyên
'''

tup = (1, 3, 5)
tup += (1, 2, 9) #tup = tup + (...)

print(tup)

tup = (3, 6, 9)
tup *= 3 #tup = tup * 3
print(tup,'\n')

#ham in kiem tra xem phan tu co nam trong Tuple hay ko
#ham len de dem so phan tu
tup = (1, ['Bao', 5], 9.1, '40', 4, ('Bao', 4.5))

a = 'Bao' in tup
b = ['Bao', 5] in tup


hamLEN= len( tup)
tup2 = tup[2:100] #lay 1 tuple ben trong 1 tuple
print('ham Len:', hamLEN)

print(a,b)
print(tup2)

tup = (1, ['Bao', 5], 9.1, '40', 4, ('Bao', 4.5))
#hàm count để đếm số lần xuất hiện của phần tử
hamCOUNT = tup.count(6.7)
#ham index trả về vị trí của phần tử trong hàm ( nếu ko có sẽ xảy ra lỗi)
hamINDEX = tup.index(4)
print(hamCOUNT, '\n',hamINDEX)









