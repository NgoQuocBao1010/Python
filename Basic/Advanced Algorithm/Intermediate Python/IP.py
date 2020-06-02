#Static and Class method

#class medthod là để chỉ các hàm được dùng khi chúng ta không cần phải tạo ra 1 object
#static method là chỉ các hàm có thể gọi mà không quan tâm đến class hay object
print("1. Class và Static method: ")

class Pet():
	numbers = 1

	def __init__(self, name, kind, age, dangerous = False):
		self.name = name
		self.age = age
		self.kind = kind
		self.dangerous = dangerous

	@classmethod
	def number_of_pet(cls):
		print(cls.numbers, '\n')

	@staticmethod
	def isOld(age):
		return age >= 5

	def describe(self):
		print(f"The {self.kind} name is {self.name}, and he is {self.age} years old!")
		if self.dangerous:
			print("Careful, he is quite sensetive with strangers!!!\n")
		else:
			print('It\'s ok, he is very friendly.\n')



newPet = Pet('Mary', 'Cat', 18)

print("Hàm classmethod: ")
Pet.number_of_pet()

print("Hàm staticmethod: ")
if Pet.isOld(newPet.age):
	print("He is Old!\n")
else:
	print("He is not Old\n")


print("Các method bình thường trong class: ")
newPet.describe()



#map function

# map là 1 phương thức dùng cho list. Dùng map để sử dụng 1 hàm cho tất cả các phần tử của list
#map trả về 1 generator nên cần ép kiểu list cho nó

# hàm  filter cũng như hàm map nhưng để áp dụng với các hàm trả về giá trị Boolean
print('2. Hàm map: ')
lst = [i for i in range(10)]

def fucn(x):
	return x + 10


print('List trước khi dùng map: ', lst, '\n')


new_lst = list(map(fucn, lst))
print("List sau khi sử dụng map để dùng hàm func cho các phần tử trong lst: ", new_lst, '\n')

print('3. Hàm Filter: ')
lst = [i for i in range(10)]

def fucn2(x):
	return x % 2 == 0

print('List trước khi dùng filter: ', lst, '\n')

new_lst = list(filter(fucn2, lst))
print("List sau khi sử dụng filter để dùng hàm func cho các phần tử trong lst: ", new_lst, '\n')


# Lambda tutorial

# Lambda là 1 hàm không tên dùng để tạo 1 hàm ngắn chỉ nhận duy nhất 1 lệnh
# Lambda có thể nhận nhiều tham số khác nhau

print('4. Hàm Lambda: ')

lst = [i for i in range(1, 10)]
print('List trước :', lst)
new_lst = list(map(lambda x: x * 3, lst))
print('List sau khi sử dụng với map và lambda:', new_lst, '\n')

print('Sử dụng hàm lambda cho 1 hàm nhỏ: ')
function = lambda x: 'is Odd' if x % 2 != 0 else 'is Even'
for element in lst:
	print(element, function(element))
print('\n\n')

# Sử dụng các Collection khác

#1. Counter:
# Counter dùng để đếm các phần tử trong 1 string, list ... và trả về 1 danh sách như là dictionary 
print('3. Collection Counter: \n')
from collections import Counter

c = Counter('I am come from Can Tho City')
print(c) 

c = Counter([1, 4, 9, 4, 10, 15, 7, 15])
print(c)

c = Counter(cats = 5, dogs = 7)
print(c, '\n\n')

print('Lấy số phần tử của cat:  ', c['cats'])

c = Counter(a = 2, b = -3, c= 2, d = 1)
# phương thức element dùng để lấy các phần tử của c dưới dạng danh sách
print('Phương thức element: ', list(c.elements()))


# phương thức most_common trả về các phần tử xuất hiện nhiều nhất trong Counter theo thứ tự
print('Phương thức most_common: ', c.most_common(2), '\n')

d = ['a', 'b', 'c', 'a', 'd']

c.subtract(d) # dùng để trừ các phần tử trong Counter bằng các phần tử trong 1 list hay tuple...
print('Hàm subtract: ', c)
c.update(d) # tương tự subtract nhưng update là thêm vào
print('Hàm update: ', c)
c.clear()
print('Hàm clear: ', c, '\n') # xóa hết phân tử

# Ta có thể giao, hợp, cộng hoặc trừ các counter, tuy nhiên khi dùng cách này thì các phần tử xuất hiện từ 0 trở xuống
c = Counter(a = 4, c = -1, b = 3, d = 0)
d = Counter(a = 2, c = 1, b = 0, d = 1)

print('Counter c + d: ', c + d)
print('Counter c - d: ', c - d)
print('Counter c giao với Counter d: ', c & d)
print('Counter c hợp với Counter d: ', c | d, '\n\n')


#2. namedtuple
# được sử dụng như để tạo 1 class

print('3. Collection namedtuple: \n')

from collections import namedtuple

Point = namedtuple('Point', 'x y z') # tạo 1 class là điểm, có tọa độ x, y, z, khai bao bằng string , phân biện bằng dấu cách

newP = Point(3, 4, 5)

print('Khai bao bằng string:', newP)
print('Tọa độ x:', newP.x)
print('Tọa độ y:', newP.y)
print('Tọa độ z:', newP.z, '\n')

Point = namedtuple('Point', ['x', 'y', 'z'] ) #khai bao bằng list, có thể bằng dictionary

newP = Point(3, 5, 7)
print('Khai bao bằng list:', newP)
print('Tọa độ x:', newP.x)
print('Tọa độ y:', newP.y)
print('Tọa độ z:', newP.z, '\n')

# phương thức fields để in ra các trường trong namedtuple
print('Phương thức fields:', newP._fields, '\n')
# phương thức replace, dùng để thay đổi 1 trường trong class namedtuple, nhưng không thay đổi trực tiếp mà trả về 1 trường khác
newP2 = newP._replace( x = 1)
print('Sau khi dùng phương thức replace:', newP2)
# phương thức make
newP2 = Point._make(['a', 'b', 'c']) # tương tự như: newP2 = Point('a', 'b', 'c')
print('\nPhương thức maka:', newP2)


#3. Collection Deque:

# Collection Deque gần giống như list nhưng ta còn có thể thao tác với cả các phần tử đầu của nó

from collections import deque
print('\n4. Collection Deque: \n')

d = deque('Chelsea')
print('Deque như là 1 list:', d, '\n')

# các phương thức:
d.append(4) # giống list
print('Phương thức append:    ', d)

d.appendleft(5) # thêm vào đầu
print('Phương thức appendleft:    ', d)

d.pop() # giống list
print('Phương thức pop:    ', d)

d.popleft() # xóa đầu
print('Phương thức popleft:     ', d)

d.extend([1, 4, 5]) # giống list, thêm vào nhiều phần tử vào cuối
print('Phương thức extend:    ', d)

d.extendleft('123') # thêm đầu
print('Phương thức extendleft:     ', d)

# phương thức rotate:
# dùng để xoay chiều các phần tử
# số dương là đem từ cuối sang đầu
# số âm là đem từ đầu sang cuối

d.rotate(3) # đem 3 phần tử cuối lên đầu
print('\nPhương thức rotate số dương:     ', d)
d.rotate(-3)
print('\nPhương thức rotate số âm:     ', d)

d.clear()
print('\nPhương thức clear:     ', d)

# ngoài ra ta có thể dùng maxlen để gán độ dài cố định cho deque
# nếu ta thêm vào quá số phần tử thì deque sẽ tự động xóa phần tử để giữ nguyên độ dài

d = deque('quocbao', maxlen = 7)
print('\n\nDeque ban đầu:     ',    d)

d.append(5) #Thêm phần tử 5 vào cuối nên deque xóa phần tử đầu để giữ độ dài là 7
print('Thêm phần tử 5 vào cuối:     ',    d)
d.appendleft('g')
print('Thêm phần tử g vào đầu:     ',    d)
