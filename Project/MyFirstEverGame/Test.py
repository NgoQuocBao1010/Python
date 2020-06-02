import pygame
import random


class Algobalon():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.step = 5
		self.jumpheight = 10
		self.jumping = False
		self.isfall = False
		self.tele = False 
		self.onthecliff = False

	def draw(self):
		pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))

	def jump(self):
		if self.jumpheight >= -10:
			if self.jumpheight < 0:
				self.isfall = True

			if not self.isfall:
				self.y = self.y - (self.jumpheight ** 2) * 0.4
				self.jumpheight -= 1
			else:
				self.fall_to_the_ground()

	def fall_to_the_ground(self, ground=True):
		if ground:
			new_height = self.y + (self.jumpheight ** 2) * 0.4
			if new_height < 410:
				self.y = new_height
				self.jumpheight += 1
			else:
				self.y = 410
				self.isfall = False
				self.jumpheight = 10
				self.jumping = False

	def teleport(self):
		self.y = 100
		self.fall_to_the_ground()
		if self.y == 410:
			self.tele = False




class cliff():
	cliffCordinate = [0, 500 - 200]

	def __init__(self, side, y):
		self.x = 0
		self.side = side
		self.y = y
		self.width = 200
		self.height = 10

	def draw(self):
		if self.side.lower() == 'l':
			pygame.draw.rect(win, (255, 0, 0), (self.cliffCordinate[0], self.y, self.width, self.height))
		else:
			pygame.draw.rect(win, (255, 0, 0), (self.cliffCordinate[1], self.y, self.width, self.height))



def updateframe():
	global scr_width, scr_height, win, hero, cliffs, cliff1
	win.fill((0, 0, 0))
	hero.draw()
	cliff1.draw()
	ground = pygame.draw.rect(win, (255, 255, 255), (0, 435, 500, 500-435))
	pygame.display.update()



def main():
    pygame.init()

    global scr_width, scr_height, win, hero, cliffs, cliff1
    scr_width = 500
    scr_height = 500
    win = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption('Algobalon The Escaper')
    clock = pygame.time.Clock()
    run = True

    hero = Algobalon(10, 410, 25, 25)
    barrier = []

    # drwa the cliff
    cliff_side = [['l', 'r', 'l'], ['r', 'l', 'r']]
    cliffs = []
    cliff_height = 320
    while run:
    	#pygame.time.delay(10)
    	clock.tick(40)

    	cliff1 = cliff('l', cliff_height)

    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			run = False

    	keys = pygame.key.get_pressed()

    	if keys[pygame.K_LEFT] and hero.x > 0:
    		hero.x -= hero.step
    	if  keys[pygame.K_RIGHT] and hero.x + hero.width < scr_width:
    		hero.x += hero.step

    	if not hero.jumping:
	    	if  keys[pygame.K_UP]:
	    		hero.jumping = True
	    	elif keys[pygame.K_a]:
	    		hero.tele = True
    	else:
	    	if hero.jumping:
	    		hero.jump()
	    	if hero.tele:
	    		hero.teleport()
    	
    	if hero.y + hero.height <= cliff1.y and 0 <= hero.x <= 0 + cliff1.width:
    		if not hero.onthecliff:
    			hero.onthecliff = True
	    		hero.y = cliff1.y - hero.width
	    		hero.jumping = False
	    		hero.jumpheight = 10
	    		hero.isfall = False
    	else:
    		if hero.onthecliff:
    			hero.fall_to_the_ground()
    		if hero.y == 410:
	    		hero.onthecliff = False


    	updateframe()

main()




