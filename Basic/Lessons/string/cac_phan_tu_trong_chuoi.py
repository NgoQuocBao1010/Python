print('1.Tui muon nhấn chữ \\n được ko')

#khi thao tác với các thư mục sẽ ảnh hưởng tới các ecscap sequnce

#cú pháp thêm 1 cái r vào trước câu lệnh. sẽ tự bơ các escape sequence

print(r'2.Tui muon nhấn chữ \\n được ko')


#có thể cộng được 2 chuỗi

str1 = 'Tôi tên là '
str2 = 'Quốc Bảo '
str3 =  str1 + '\n' + str2
print(str3)
print('\n')
#python ho tro phep nhan cac chuoi

str4 = str2*5 
print(str4)
print('\n')

#in: dùng để kiểm tra 1 chuỗi có nằm trong 1 chuỗi khác hay không
# lấy ký tự giống lấy phần tử trong mảng bên C++
#nếu lấy số âm thì python sẽ dò ngược lại từ phần tử cuối
# dùng ham len(strA) để lấy độ dài chuỗi
#cắt chuỗi của python
strA = 'Toi co 1 cây dao'
strB = 'dao'
strC = strA[-2]
strD = strA[2:15]
strE = strB in strA
strF = strA[None:None:2] #cái cuối cùng là bước nhảy

print(strE) 
print(strC)
print(strD)
print(strF) 
print('\n')

#ép kiểu

stra = "69"
strb = int("69") + 7 #ép từ chuỗi thành số
strc = int (6.9) # lấy phần nguyên

print(stra)
print(strb)
print(strc)   

#không thể thay đổi 1 phần tử trong chuỗi 1 cách trực tiếp
#phải thay đổi gián tiếp
print('\n')
strH = 'Toi thích MU' #chuyển thành Toi thích MC

strH = strH[None:-1] + 'C' 

strG = 'Moderfucker' #chuyển thành Moderf***er

strG = strG[None:6] + '***' + strG[-2:None]
print(strH)
print(strG)