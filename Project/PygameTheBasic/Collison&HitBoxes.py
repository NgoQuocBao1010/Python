import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First game')
clock = pygame.time.Clock()
score = 0


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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

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

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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


class enemy(object):
    E_walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    E_walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = (self.x, self.end)
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, surface):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.E_walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.E_walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1] :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health) ), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def gethit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False



# character picture
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redrawwin():

    win.blit(bg, (0,0)) # import a background picture
    text = score_font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    p1.draw(win)
    monster.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#mainloop
score_font = pygame.font.SysFont('comicsans', 30, True)
p1 = player(300, 410, 64, 64)
monster = enemy(100, 410, 64, 64, 450)
shootloop = 0
bullets = []

run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        if p1.right:
            fac = 1
        else:
            fac = -1

        if len(bullets) < 6:
            bullets.append(projectile(round(p1.x, p1.width //2), round(p1.y + p1.height//2), 6, (0,0,0), fac))
        shootloop = 1

    for bullet in bullets:
        if bullet.y - bullet.radius < monster.hitbox[1] + monster.hitbox[3] and bullet.y + bullet.radius > monster.hitbox[1]:
            if bullet.x + bullet.radius > monster.hitbox[0] and bullet.x - bullet.radius < monster.hitbox[0] + monster.hitbox[2]:
                monster.gethit()
                score += 50
                bullets.pop(bullets.index(bullet))

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
