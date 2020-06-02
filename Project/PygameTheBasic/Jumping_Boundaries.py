import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First game')

x = 50
y = 400
width = 40
height = 60
vel = 5

jump = False
jump_hght = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if not jump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height :
            y += vel
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

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
