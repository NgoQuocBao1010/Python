#ham dùng để cập nhật

a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
print(a, '\n')


#thêm vào cuối list 1 phần tử 
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
a.append(['CR7', 4.5])
print(a, '\n')

# tách từng phần tử trong list để thêm vào list
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
a.extend(['CR7', 4.5])
print(a, '\n')

#thêm 1 phần tử vào vị trí i
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
a.insert(3, 'Hola')
a.insert(-1, 5)
print(a, '\n')


# bỏ ra 1 phần tử rồi trả về giá trị đó
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
c = a.pop(4)
print(c)
print(a, '\n')

# bỏ ra phần tử đầu tiên có giá trị x trong list (NẾU như ko có sẽ bị lỗi)
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
a.remove(5.6)
print(a, '\n')

#đảo ngược list
a = [3, 5.6, 75, 'Bao', [5, 'Chelsea'] ]
a.reverse()
print(a, '\n')

''' hàm sắp xếp list theo từ bé đến lớn hay từ lớn đến bé
	list có các phần tử cùng kiểu dữ liệu
'''
a = [3, 5.6, 75, 5 ]
a.sort() #bé tới lớn
print(a, '\n')

a = [3, 5.6, 75, 5 ]
a.sort(reverse=True) #lớn tới bé
print(a, '\n')

a = ['BaoQuocNgoHOngzz', 'Chelsea', 'Ngày mai', 'Chào' ]
a.sort(reverse=True)
print(a, '\n')


# tách 1 cụm TỪ (STTRING)trong list và cho từng từ là 1 phần tử của list mới
a = '34 67 55 33 1298'
ptu = a.split()

print(a)
print(ptu)

