import pygame
import math

char = pygame.image.load('Attemp4.png')
magic_door = pygame.image.load('MagicDoor.png')

class TheHero():
	sth_to_step_on = [470, 200]
	that_th_range = [(0, 500), (0, 150)]
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 64
		self.height = 60
		self.step = 5
		self.falling = False
		self.can_stand = True
		self.move_to_left = True
		self.move_to_right = True
		self.on_the_air = False
		self.frame_fall = 0

	def draw(self):
		win.blit(char, (self.x, self.y))

	def check_if_movable(self):
		feet = self.y + self.height
		print(feet)
		if feet not in self.sth_to_step_on:
			self.can_stand = False
			return
		else:
			self.can_stand = True
			index = self.sth_to_step_on.index(feet)

		print(index, self.x)

		if index == 0:
			if self.that_th_range[0][0] > self.x:
				self.move_to_left = False
			else:
				self.move_to_left = True

			if self.that_th_range[0][1] < self.x + self.width:
				self.move_to_right = False
			else:
				self.move_to_right = True
		else:
			if self.that_th_range[index][0] > self.x:
				if self.x > 0:
					self.can_stand = False
					self.falling = True
				else:
					self.move_to_left = False

			if self.that_th_range[index][1] < self.x + self.width:
				if self.x + self.width < 500:
					self.can_stand = False
					self.falling = True
				else:
					self.move_to_right = Falsed

	def fall(self, ground=True):
		if ground:
			if not self.on_the_air:
				feet = self.y + self.width
				time = math.sqrt((470 - feet) * 2 * 0.1)
				self.frame_fall = time / 4
				self.on_the_air = True

			if self.on_the_air:
				if self.y + self.width < 470:
					self.y += 0.5 * 10 * self.frame_fall * self.frame_fall
				elif self.y + self.width  == 470:
					self.falling = False
					self.on_the_air = False
					self.can_stand = True


class magicdoor():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.hitbox = (self.x, self.y, 55, 64)

	def draw(self):
		#pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
		win.blit(magic_door, (self.x, self.y))


class thebullet():
	def __init__(self, x, y, radius=10):
		self.x = x
		self.y = y
		self.radius = radius
		self.step = 5

	def draw(self):
		pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)


def reDraw():
	win.fill((255,255,255))
	pygame.draw.rect(win, (0, 0, 0), (0, 200, 150, 20))
	bao.draw()
	md.draw()
	for bullet in bullets:
		bullet.draw()
	pygame.display.update()


def main():
	global win, bao, md, bullets
	pygame.init()

	scr_width = 500
	scr_height = 500
	win = pygame.display.set_mode((scr_width, scr_height))
	pygame.display.set_caption('Doraemon')
	clock = pygame.time.Clock()

	run = True

	bao = TheHero(100, 410)
	md = magicdoor(400, 410)
	bullets = []
	shoot_wait = 0

	while run:
		clock.tick(27)

		bao.check_if_movable()

		if shoot_wait > 0:
			shoot_wait += 1
		if shoot_wait > 5:
			shoot_wait = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		if not bao.can_stand:
			bao.fall()

		if keys[pygame.K_SPACE] and shoot_wait == 0:
			if len(bullets) < 4:
				bullets.append(thebullet(bao.x + bao.width, bao.y + bao.height //2))
			shoot_wait = 1

		for bullet in bullets:
			if bullet.x + bullet.radius < 500 and bullet.x -bullet.radius > 0:
				bullet.x += bullet.step
			else:
				bullets.pop(bullets.index(bullet))

		if bao.can_stand:
			if keys[pygame.K_a] and bao.move_to_left:
				bao.x -= bao.step
			elif keys[pygame.K_d] and bao.move_to_right:
				bao.x += bao.step


		if bao.x + bao.width > md.hitbox[0]:
			bao.x = 10
			bao.y = 200 - bao.height

		print(5)
		print(bao.x, bao.y + bao.height, bao.falling, bao.can_stand, bao.move_to_left)
		reDraw()


main()


