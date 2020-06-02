dic = {'Name' : 'Quoc Bao', 'PersonalInfo' : ['Chelsea', 9.1], 'age' : 19}

print(dic)
print(type(dic), '\n')

#constructor dict

dic  = {}
print(type(dic), '\n')

inter = [('Name', 'Quoc Bao'), ('PersonalInfo', ['Chelsea', 9.1]), ('age', 19)]
dic = dict(inter) # chỉ cần list hoặc tuple đó dữ liệu có đủ cả key như Name và get item như Quoc Bao
print(dic)
print(type(dic), '\n')


# khởi tạo dict dùng biến

dic = dict(name = 'Son Tung', age = '23') # name và age là biến

name = 'Bao' # gán hàm age và name cho 1 giá trị khác ở bên ngoài dict
age = '19'

print(dic, '\n\n') # in ra sẽ thấy name và age ở trong dict không bị thay đổi



#ham 

inter = ('Name', 'Age', 'Score', 45)

dic = dict.fromkeys(inter) # hàm dict.fromkeys truyền dữ liệu vào các key để tạo dict, mặc định là NOne
print(dic)

dic = dict.fromkeys(inter, 'Bao') # bây giờ sẽ truyền dữ liệu là Bao cho các key
print(dic, '\n\n')


# lấy các phần tử trong dic bằng cách dùng key
# nếu key không tồn tại sẽ báo lỗi
dic = {'Name' : 'Quoc Bao', 'PersonalInfo' : ['Chelsea', 9.1], 'age' : 19, 40  : 'Bao'}

print(dic['PersonalInfo'][1])
print(dic['Name'])
print(dic[40], '\n\n')

# dict là 1 unhashable  nên có thể thay đổi các phần tử

dic = {'Name' : 'Quoc Bao', 'PerInfo' : ['Chelsea', 9.1], 'age' : 19, 40  : 'Bao'}

dic['Name'] = 'Hazard'
dic[40] += 'Ngo' # có thể cộng thêm giá trị
print(dic)
dic['phone'] = 'Note 8' # nếu thay đổi 1 phần tử không có sẵn trong dic thì sẽ tự thêm phần tử đó vào dic
print(dic)









