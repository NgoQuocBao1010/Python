#cac phuong thuc 
dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19]}
dic1 = dic.copy() #tao 1 ban sao
print(dic)
print(dic1, '\n\n')


dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19]}
dic.clear()
print(dic1, '\n\n')


dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19]}
value = dic.get('Name') # lấy giá trị cảu phần tử theo key, khi khonong có key hoặc không có dữ liệu thì sẽ trả  về none
value1 = dic.get('Mother\'s Name')
value2 = dic.get('Mother\'s Name', 'Không có thông tin') # không có sẽ trả về thông tin ở phía sau

print(value)
print(value1)
print(value2, '\n\n')


dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19]}

value = dic.items() # tạo 1 kiểu dữ liệu dict_item trong đó có tuple với phần tử thứ nhất trg tuple là keys còn cái còn lại là value
print(value)
print(type(value), '\n')

value = tuple(value) # ép thành dữ liệu tuple để lấy phần tử
print(value[0][1], '\n')

value = dic.keys() # tạo ra kiểu dữ liệu dict_item để lưu các key
value1 = dic.values() # tạo ra kiểu dữ liệu dict_item để lưu các phần tử

print(value)
print(value1, '\n\n')


dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19], 'Goals' : 18}

value = dic.pop('Info') # xóa key và value trong dict rồi trả về 1 list có 2 phần tử là key và value đó, nếu không dò thấy key sẽ báo lỗi
value1 = dic.pop('Assist', 'Không tìm thấy dữ liệu') # không tìm thấy trả ra hàm default

print(value)
print(value1)
print(dic, '\n\n')



dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19], 'Goals' : 18}

value = dic.setdefault('Goals') # lấy value trong 1 key
print(value, '\n')

value = dic.setdefault('Assist') # nếu không có thì sẽ tự thêm key đó và cho giá trị là none vào dict
print(value)
print(dic, '\n')

dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19], 'Goals' : 18}
value = dic.setdefault('Assist', '10') # nếu không có thì sẽ tự thêm key đó và cho giá trị bằng hàm default
print(value)
print(dic, '\n')

print('\nHàm update')

# dùng để update các phần tử trong dict với điều kiện các dữ liệu dùng để update phải có 1 phần tử làm key và cái còn lại làm value
dic = {'Name' : 'Odoi', 'Info' : ['Chelsea', 19], 'Goals' : 18}

A = {'Assist': 15}
dic.update(A)
print(dic)

E = ([3,4], [5.6, 8])
dic.update(E)
print(dic)

F = {('Quoc', 'Bao'), ('Ngo', 'Hong')}
dic.update(F)
print(dic)

dic.update(Name= 'Pulisic')
print(dic)

H = {'Name' : 'Reece James', 'Info' : 'Injured' }
dic.update(H)
print(dic)








