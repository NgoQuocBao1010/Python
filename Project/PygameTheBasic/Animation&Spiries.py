import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First game')
clock = pygame.time.Clock()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
#char = pygame.image.load('baobao.png')

x = 50
y = 400
width = 64
height = 64
vel = 5

# character attributes
jump = False
jump_hght = 10

left = False
right = False

walkCount = 0


def redrawwin():
    global walkCount

    win.blit(bg, (0,0)) # import a background picture
    
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


#mainloop
run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        fall_down = 1
        if jump_hght >= -10:
            if jump_hght < 0:
                fall_down = -1
            y -= (jump_hght ** 2) * 0.5 * fall_down
            jump_hght -= 1
        else:
            jump_hght = 10
            jump = False
    redrawwin()

pygame.quit()
