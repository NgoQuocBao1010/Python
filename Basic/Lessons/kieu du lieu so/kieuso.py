a = 309099-98
print(a)
print(type(a))

#python khong gioi han du lieu so nguyen
#số thực python chỉ lấy tới 15 chữ số sau dấu chấm

# muốn lấy hơn 15 chữ số sau dấu chấm thì phải thêm từ thư viện

#lấy nội dung từ thư viện decimal
from decimal import*

#lấy tối đa 30 chữ số = chữ số nguyên và phần thập phân
getcontext().prec = 20

f = 10/3
print(f) #không có Decimal
print(type(f))

f1 = Decimal(10)/3 #có Decimal
print(f1)
print(type(f1))


m = 15 
n = 47

print(n // m) #lấy thương nguyên
print(m ** n) #lũy thừa
print(n % m) # số dư




a = 1/3

print(round(a))






