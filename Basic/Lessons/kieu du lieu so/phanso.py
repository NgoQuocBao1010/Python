#phải thêm thư viện fractions vào để tạo phân số

from fractions import*

frac = Fraction(6,9)
print(frac) #python khi in ra sẽ tự rút gọn
print(type(frac))

f2 = Fraction(9, 6)
f3 = Fraction(7, 5)

f3 = frac + f2 + f3

print(f3)