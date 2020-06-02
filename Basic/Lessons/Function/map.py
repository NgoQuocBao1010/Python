# map sẽ trả về một generator nên cần thêm constructor cho nó
func = lambda x : x + 1

lst = [i for i in range(0,10)]
print(lst)
lst = list(map(func,lst)) # sử dụng hàm lambda cho lst
print(lst)


lst = [-2, 5, 7, 8.1]
lst1= [0, 6, 7, 3]

newlst = list(map(lambda x,y: x + y, lst, lst1)) # cộng giá trị từ 2 list

print(newlst)
print('\n\n')

# hàm filter dùng để lọc có điều kiện

lst = [-1, 3, -4, 5, -1.1]
print(lst)
newlst = list(filter(lambda x: x >= 0, lst)) # lọc các phần tử nhở hơn 0
print(newlst)
print('\n\n')

# hàm reduce ( cần phải import từ thư viện functools)
from functools import reduce

# reduce (fuction, sequence, parameter initial)
'''Hàm reduce sẽ trả về 1 giá trị
	Nếu không có parameter initial thì hàm reduce sẽ lấy 2 giá trị đầu của lst đưa vào func rồi đem giá trị tiếp theo đưa vào
	Nếu có thì sẽ đưa parameter trước rồi làm y chang'''

lst = [0, 1, 3, 5, 7, 9]


print(reduce(lambda x, y: x + y, lst)) #tinh tong
print(reduce(lambda x, y: x + y, lst, 10)) # them initial parameter vao



'''
~ Maybe the time flies away so fast,
~ Leave me your picture in the past,
~ The memories I try to keep in me,
~ You gave me the world I want to see,

~ Beside you forever is my desire,
~ When I am weak, you give me the fire,
~ But the memories will turn into whispers,
~ Someday the beautiful flowers will wither,

~ My heart, my world was flooded in tears,
~ I scream in desperation, but no one hears,
~ My heart break in pain, sadness embraces,
~ Remember your smile, tears cover my face,

~ Lonely melodies echo in my heart,
~ The sky has only mourning doves,
~ Grieving, my heart was torn apart,
~ Cold raindrops over the sky above,

~ Maybe time goes by really fast,
~ Maybe tears cannot solve anything,
~ Maybe everything I want is too far,
~ Maybe now the effort is just nothing,

~ But all is enough to remember,
~ The moments we are together,
~ All will be part of my heart forever,
~ A love we have for each other,

~ Thank you for letting me know what love is,
~ Even though you are not here, you still alive in my heart,


-Brian '''


