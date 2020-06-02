import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First game')
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jump_hght = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, surface):
        if p1.walkCount + 1 >= 27:
            p1.walkCount = 0

        if p1.left:
            surface.blit(walkLeft[p1.walkCount//3], (p1.x, p1.y))
            p1.walkCount += 1
        elif p1.right:
            surface.blit(walkRight[p1.walkCount//3], (p1.x, p1.y))
            p1.walkCount += 1
        else:
            surface.blit(char, (p1.x, p1.y))


# character picture
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redrawwin():

    win.blit(bg, (0,0)) # import a background picture
    p1.draw(win)
    pygame.display.update()


#mainloop
p1 = player(300, 410, 64, 64)
run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and p1.x > 0:
        p1.x -= p1.vel
        p1.left = True
        p1.right = False
    elif keys[pygame.K_RIGHT] and p1.x < 500 - p1.width:
        p1.x += p1.vel
        p1.left = False
        p1.right = True
    else:
        p1.left = False
        p1.right = False
        p1.walkCount = 0

    if not p1.jump:
        if keys[pygame.K_SPACE]:
            p1.jump = True
    else:
        fall_down = 1
        if p1.jump_hght >= -10:
            if p1.jump_hght < 0:
                fall_down = -1
            p1.y -= (p1.jump_hght ** 2) * 0.5 * fall_down
            p1.jump_hght -= 1
        else:
            p1.jump_hght = 10
            p1.jump = False
    redrawwin()

pygame.quit()
