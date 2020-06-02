a = 'my name is Quoc Bao'

b = a.capitalize() #viet hoa chu cai dau va viet thuong cac chu con lai

c = a.upper() #viet chu in het toan bo

d = a.lower()

e = a.swapcase() #chu viet thuong thi viet hoa con chu viet hoa thi viet thuong

f = a.title() #viet hoa moi chu cai

# cu phap center(width, [fillchar]) fillchar la 1 chuoi co do dai la 1
g = a.center(30, '&') #can giua

h = a.rjust(45, '#') #can phai (can trai la l.just)


#encode la ma hoa

A = ' tên Bảo. '
B = A.encode()

# cộng danh sách vào các chuỗi
C = A.join(('Tui', 'Tao', 'Tớ', ''))

#replace

D = a.replace('m', 'H') #thay the het
E = a.replace('m', 'H', 1) #thay the 1 lan

# hàm split('[ký tự cắt]', '[số lần cắt]')
karma = 'My favorite club is Chelsea'
F = karma.split(' ')
G = karma.rsplit(' ', 2) #cắt từ bên phải

#hàm partition chia cắt 1 chuỗi từ 1 chuỗi ở giữa

H = karma.partition('club')

#hàm count đếm số chuỗi có trong chuỗi count('chuỗi',  ,   ) 

J = karma.count('e')
K = karma.count('e', 0, 15) #phạm vi

#hàm startswith và endswith trả về true hoặc False để kiếm coi giá trị đó có đứng đầu không

L = karma.startswith('M')
Z = karma.startswith('M', 3) #tính từ vị trí số 3

#hàm find để tìm 1 chuỗi trong 1 chuỗi rồi trả về vị trí của phần tử đầu tiên trong chuỗi cần tìm
# hàm index cũng giống hàm find nhưng nếu không tìm thấy thì sẽ trả về lỗi
#hàm rfind và rindex để tìm từ bên phải sang
X = karma.find("Che")
V = karma.index("vori")

#hàm islower(), isupper() để check xem TOÀN BỘ chuỗi có được viết thường hay hoa không
#hàm isdigit để kiểm tra chuỗi có phải số ko
#hàm isspace để kiểm tra TOÀN BỘ chuỗi có phải là khoảng trắng hay không
N = karma.islower()

# do dai cua chuoi
hamLEN = len(karma)



print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(J)
print(K)
print(L)
print(Z)
print(X)
print(V)
print(N)
print(hamLEN)