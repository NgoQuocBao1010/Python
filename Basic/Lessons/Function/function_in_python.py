# hàm cơ bản:

def numbers(a = 0): #(hàm default a = 0 sẽ chạy khi không truyền giá trị cho a và hàm default phải ghi ở cuối )
	if a > 0:
		print('This number is a positive number')
	elif a < 0:
		print('This is a negative number')
	else :
		print('This is not neither positive or negative number')


a = 5

numbers(-7)
numbers(9.3)
numbers(0)
numbers() # nếu không điền gì vào thì sẽ sử dụng hàm default ở trên là a = 0 
print('\n')



def Maximum(lst=[]):
	if len(lst) == 0:
		print('This is an empty list!')
	else:
		max = lst[0]
		for i in range(len(lst)):
			if (lst[i] > max):
				max = lst[i]
		return max


lst = [1, -6 , 0, 7 , 11]
Maximum(lst)
print(Maximum(lst))

print('\n')


# TRONG HÀM CỦA PYTHON TA KHÔNG CẦN PHẢI TRUYỀN DỮ LIỆU THEO THỨ TỰ MÀ CÓ THỂ TRUYỀN THEO KEY

def sum3num(a, b = 3, c = 2):
	print(a,'+',b,'+',c,'=', a + b +c)


sum3num(1, 4, 2) # truyền theo thứ tự

sum3num(b = 8, a = -7 , c = 10) # truyền theo key a, b, c không cần theo thứ tự

sum3num(c = 3, a = -1) # trường hợp không truyền thì b lấy hàm dèfault





def sum4num(a, *, b, c = 1, d = -1): # phía sau * phải đưa khai báo bằng key
	print(a,'+',b,'+',c,'+',d,'=', a + b +c+d)

sum4num(1, b = 2 ,c =3, d =4)

print('\n')


# LẤY CÁC PHẦN TỬ TRONG LIST HAY TUPLE MÀ KHÔNG CẦN DÙNG 'FOR I'

lst1 = [ 8, 5, 7] 
tup1 = (3, 5)
sum3num(*lst1) # không dùng cho các hàm buộc sử dụng key như hàm sum4num ở trên
sum3num(*tup1, 8) # nếu không đủ các phần tử hoàn toàn có thể thêm vào

print('\n')



#NẾU CHÚNG TA KHÔNG BIẾT CÓ BAO NHIÊU THAM SỐ CẦN ĐƯA VÀO TA HOÀN TOÀN CÓ THỂ SỬ DỤNG * ĐỂ GÓI CÁC THAM SỐ LẠI THÀNH 1 TUPLE
 
def printEle(*ele):
	print(ele)
	for i in range(len(ele)):
		print('Phần tử thứ', i+1,'là:',ele[i])

printEle('Bao', 5, 6.1, 9, ['23', (4, 5.6)]) # goí các phần tử này thành 1 tuple
print('\n')


''' SỬ DỤNG HÀM CHO DICTIONARY 
	NẾU CHỈ UNPACK BÌNH THƯỜNG THÌ CHỈ LẤY ĐƯỢC CÁC KEY
	NẾU MUỐN LẤY CÁC VALUE THÌ CÁC THAM SỐ TRUYỀN VÀO BUỘC PHẢI GIỐNG VỚI KEY TRONG DIC
	VÀ CẦN PHẢI UNPACK DIC 2 LẦN, SỬ DỤNG 2 DẤU *''' 


def value_in_dictionary(Name, Age): # Name và age giống trong Dic
	print(Name)
	print(Age)

dic = {'Name' : 'Pulisic', 'Age': '19'}
value_in_dictionary(**dic) # sử dụng 2 *



# TẠO 1 DICT TRONG BẰNG FUCTION
def dictionary(**dic1):
	print(dic)
	print(type(dic))


dictionary(name = 'Mason Mount', age = '18')
print('\n')

# Yield

def tripleEl(lis):
	for element in lis:
		yield element * 3

tup = tripleEl((1, 5, 6))

for value in tup:
	print(value)
print('\n')

'''def what_the_hell_is_this():
	return 'Quoc Bao'
	
	return 'Tammy'


ksi = list(what_the_hell_is_this())
print(ksi)



'''



