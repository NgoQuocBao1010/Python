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
        self.standing = True

    def draw(self, surface):
        if p1.walkCount + 1 >= 27:
            p1.walkCount = 0

        if not self.standing:
            if p1.left:
                surface.blit(walkLeft[p1.walkCount//3], (p1.x, p1.y))
                p1.walkCount += 1
            elif p1.right:
                surface.blit(walkRight[p1.walkCount//3], (p1.x, p1.y))
                p1.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing=-1):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

        
# character picture
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redrawwin():

    win.blit(bg, (0,0)) # import a background picture
    p1.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#mainloop
p1 = player(300, 410, 64, 64)
bullets = []

run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if p1.right:
            fac = 1
        else:
            fac = -1

        if len(bullets) < 6:
            bullets.append(projectile(round(p1.x, p1.width //2), round(p1.y + p1.height//2), 6, (0,0,0), fac))

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_LEFT] and p1.x > 0:
        p1.x -= p1.vel
        p1.left = True
        p1.right = False
        p1.standing = False
    elif keys[pygame.K_RIGHT] and p1.x < 500 - p1.width:
        p1.x += p1.vel
        p1.left = False
        p1.right = True
        p1.standing = False
    else:
        p1.standing = True
        p1.walkCount = 0

    if not p1.jump:
        if keys[pygame.K_UP]:
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
