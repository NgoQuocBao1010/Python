import pygame
import random

class cube(object):
	rows = 20
	width = 500

	def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
		self.pos = start
		self.dirnx = 1
		self.dirny = 0
		self.color = color

	def move(self, dirnx, dirny):
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos   = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny) 

	def draw(self, surface, eyes=False):
		distance = self.width // self.rows

		start = self.pos[0]
		end   = self.pos[1]

		pygame.draw.rect(surface, self.color, (start*distance + 1, end*distance + 1, distance-2, distance-2))


class snake(object):
	body = []
	turns = {}

	def __init__(self, color, pos):
		self.color = color
		self.head = cube(pos,color=self.color)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

		for index, cube in enumerate(self.body):
			position = cube.pos[:]
			if position in self.turns:
				turn = self.turns[position]
				cube.move(turn[0], turn[1])
				if index == len(self.body) - 1:
					self.turns.pop(position)
			else:
				if cube.dirnx == -1 and cube.pos[0] <= 0: 
					cube.pos = (cube.rows-1, cube.pos[1])
				elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1: 
					cube.pos = (0,cube.pos[1])
				elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1: 
					cube.pos = (cube.pos[0], 0)
				elif cube.dirny == -1 and cube.pos[1] <= 0: 
					cube.pos = (cube.pos[0],cube.rows-1)
				else: 
					cube.move(cube.dirnx,cube.dirny)

	def draw(self, surface):
		for index, cube in enumerate(self.body):
			if index == 0:
				cube.draw(surface, True)
			else:
				cube.draw(surface)

	def addCube(self):
		tail = self.body[-1]
		dx, dy = tail.dirnx, tail.dirny
 
		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
		elif dx == 0 and dy == -1:
			self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy



def randomFood():
	x = random.randrange(rows)
	y = random.randrange(rows)

	return x, y


def drawgrid(width, rows, surface):
	distance = width // rows
	vertical_line = 0
	horizontal_line = 0

	for line in range(rows):
		vertical_line += distance
		horizontal_line += distance

		pygame.draw.line(surface, (255, 255, 255), (vertical_line, 0), (vertical_line, width))
		pygame.draw.line(surface, (255, 255, 255), (0, horizontal_line), (width, horizontal_line))


def redrawwin(surface):
	global width, rows, food, my_sn
	surface.fill((0,0,0))
	my_sn.draw(surface)
	food.draw(surface)
	drawgrid(width, rows, surface)
	pygame.display.update()


def main():
	global width, rows, food, my_sn
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	clock = pygame.time.Clock()

	run = True
	food = cube(randomFood(), color=(0, 255, 0))
	my_sn = snake(pos=(10,10),color=(0, 0, 255))

	while run:
		pygame.time.delay(50)
		clock.tick(5)
		my_sn.move()

		if my_sn.body[0].pos == food.pos:
			my_sn.addCube()
			food = cube(randomFood(), color=(0, 255, 0))
		redrawwin(win)
	pass


main()
