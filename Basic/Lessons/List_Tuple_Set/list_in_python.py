''' giới hạn bởi []
cac phần tử trong LISt cách nhau bởi dấu ,
List có khả năng chứa mọi giá trị đối tượng bao gồm chính nó
'''

list_rong = [] #list rỗng

p = [5, 6, 6.7, 6.7, 'Quoc Bao']

a = [i for i in range(30)] # tạo list trong đó i là các phần tử lấy từ 0 đến 30 phần tử

b = [[m, m + 1, m*2] for m in range(1,5)]

'''
Hàm List
ở trong phải là interable(tap hợp nhiều phần tử)
Ví dụ: int 1 ko phải là interable; 'hello' là 1 interable
'''
c = list('hello')


r = p + ['Iron Man', 56] #toan cộng trong list (lưu ý chỉ cộng các list được với nhau)

j = p * 2 #có thể x list lên nhiều lần nhưng không theer x các list với nhau


#hàm in để xem có phần tử trong list hay ko
hamIN = 'Quoc Bao' in p
#hàm count để đếm số lần xuất hiện của phần tử
hamCOUNT = p.count(6.7)
#ham index trả về vị trí của phần tử trong hàm ( nếu ko có sẽ xảy ra lỗi)
hamINDEX = p.index(5)
# hàm copy tạo ra 1 bản sao giống list trước (có thể sủa được ko ảnh hưởng đến list cũ)
hamCOPY = p.copy()
# hàm clear để xóa các phần tử trong list








''' Cách lấy phần tử trong list
'''

list_moi = [1, 3.5, 'Quoc', 'Bao', 'Quoc Bao', [5, 'Chelsea', '67.6']]

layphantu = list_moi[0]

lpt1 = list_moi[3]

lpt2 = list_moi[5][-1] # dấu trừ là lấy từ bên phải sang

lpt3 = list_moi[1 : 3] # lấy từ phần tử thứ nhất và không lấy phần tử cuối (không điền sẽ lấy từ đầu hoặc lấy tới cuối)

#đổi pt trong list
list_moi[2] = 'Xin Chao'

#ma trận cơ bản

matran = [[1,2,3], [4,5,6], [6,7,8]]

# không được gán list này qua list khác bởi vì 1 list là 1 con trỏ

list_1 = [1,2,3]
list_2 = list_1
list_3 = list(list_1)


list_2[0] = "Chao" #thay đổi giá trị của 1 list sẽ thay đổi giá trị của cả 2 list
list_3[0] = "Hello" #sửa bằng cách cho list bằng khởi tạo của list kia








print(p)
print('\n')
print(a)
print('\n')
print(b)
print('\n')
print(c)
print('\n')
print(r)
print('\n')
print(j)
print('\n')
print(hamIN)
print(hamCOUNT)
print(hamINDEX)
print(hamCOPY)

print('\n')
print(layphantu)
print(lpt1)
print(lpt2)
print(lpt3)
print(list_moi)
print('\n')
print('Đây là Ma Trận')
print(matran[0])
print(matran[1])
print(matran[-1])
print('Truy xuat phan tu')
print(matran[2][1])
print('\n')
print('list_2 bị thay đổi sẽ ảnh hưởng tới list_1 nếu gán 2 list cho nhau')
print(list_1)
print(list_2)
print(list_3)