#phần trăm %s = string

a = 'My name is %s' %('Quoc Bao')

print(a)

b = 'The clubs that I love are %s and %s' %('Chelsea' , 'Juventus')

print(b)

c = 'My most favorite player in the world is %s'
print(c %('Cristiano Ronaldo'))

d = c %('Eden Hazard')
print(d)
print('\n')

#phân trăm %d, %f
e = 'Toi có %d đồng' #có thể sủ dụng %s cho dữ liệu ngoài sstr
f = 'Toi có %.2f đồng'

print(e %(45.598))
print(f %(45.598))
print('\n')

#sử dụng hàm f để kiếm hàm khác đưa vào
#muon in {ten} ra thi in la {{ten}}
Sodienthoai = '0939983979'
Tenho = 'Quoc Bao'
Tinhtrang = 'Bi duoi hoc'

result = 'Hoc sinh {Tenho} co so dien thoai la {Sodienthoai}\n{Tinhtrang} '
resultf = f'Hoc sinh {Tenho} co so dien thoai la {Sodienthoai}\n{Tinhtrang} '

print(result)
print(resultf)
print('\n')
#dinh dang bang phuong thuc Format

DStienthuong = 'Ban A duoc {} dong. Ban B duoc {} dong. Ban C duoc {} dong\n'.format(10000, 2343242, 300000, 35534)
DStienthuong1 = 'Ban A duoc {1} dong. Ban B duoc {1} dong. Ban C duoc {3} dong\n'.format(10000, 20000, 300000, 352344) #số ở trong {} la so thu tu
DStienthuong2 = 'Ban A duoc {first} dong. Ban B duoc {second} dong. Ban C duoc {last} dong\n'.format(first=10000,second= 20000,last= 300000) # o trong {} la ten
print(DStienthuong)
print(DStienthuong1)
print(DStienthuong2)

'''su dung format de can le'''

cangiua = 'Cau lac bo {:*^50}'.format('Chelsea')
canletrai = 'Cau lac bo {:<50}'.format('Chelsea')
canlephai = 'Cau lac bo {:*>50}'.format('Chelsea')
print(cangiua)
print(canletrai)
print(canlephai)

print('\n')
a = 15
print('%d' %(a))