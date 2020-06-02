import turtle
import random

john = turtle.Turtle()

# chọn màu cho hình cần vẽ (màu stroke, màu fill)
john.color('red', 'blue')

# chọn độ rộng của đường vẽ
john.width(5)

# vẽ 1 hình tròn
john.begin_fill()
john.circle(50) # 100 là đường kính
john.end_fill()

# di chuyển đi chỗ khác
john.penup()
john.right(45)
john.forward(150)
john.left(45)
john.pendown()

# Ta không thể vẽ hình khác bằng cách dùng phương thức như hình tròn
# Ví dụ: Vẽ hình vuông:

john.color('black', 'purple')

john.begin_fill()
for time in range(4):
    john.forward(70)
    john.right(90)
john.end_fill()

# Vẽ các hình ở các vị trí khác nhau trên màn hình

colors = ['red', 'yellow', 'orange', 'green', 'blue', 'black', 'pink']

for time in range(10):
    john.color(random.choice(colors), random.choice(colors))
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    john.penup()
    john.setpos((x, y))
    john.pendown()
    john.begin_fill()
    john.circle(random.randrange(10, 60))
    john.end_fill()
