
''' Biến Local
	Khi tạo 1 biến trong 1 hàm (biến đó gọi là Local) thì bản chất là nó sẽ copy các giá trị từ bên ngoài vào
	Nên thay đổi giá trị biến Local sẽ không ảnh hưởng bên ngoài
	và khi gọi biến Local đó ở ngoài hàm thì chương trình sẽ không nhận'''

name = "Pulisic"
Age = 19

def changeValue(parameter): # hàm dùng để đổi các tham số thành None và khi đổi xong thì in ra Change Sucessfully
	parameter = None;
	print('{:*^30}'.format("Change Sucessfully!"))

changeValue(name)  
changeValue(Age)

print(name) # đã in ra Change Sucessfully nhưng các biến name và Age ko thay đổi bởi vì biến parameter chỉ đơn giản là copy chứ không thay đổi thực sự
print(Age)
print('\n')
# cách thay đổi các biến Local, ta dùng hàm global

''' Biến Global
	Nếu khai báo biến global thì có thể xài bất kỳ đâu'''


def greeting():
	global greet # khai báo biến greet bên trong hàm
	greet = 'Xin Chao'
	print(greet)

greeting()
print(greet) # vẫn dùng được ở ngoài sau khi chạy hàm
print('\n')

#print(globals()) # in ra các biến global trong chương trình
#print(locals()) # in ra các biến global trong chương trình
