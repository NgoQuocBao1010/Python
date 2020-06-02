import pygame
import random
import os
import shelve

# Screen config
width  		= 800
height 		= 500
game_title 	= 'Space Traveler'

#project images
images_path  	= os.path.join(os.getcwd(), 'images')
character_img 	= pygame.image.load(os.path.join(images_path, "spaceship.png"))
health_img		= pygame.image.load(os.path.join(images_path, "heart.png"))
healthless_img	= pygame.image.load(os.path.join(images_path, "heartless.png"))

#============================= Game Score Management ==============================#
def saveTheScore(score):
	data = {'boo' : 1000, 'choo': 500, 'loo': 300}
	with shelve.open('.\\highscores\\highscores') as f:
		data.setdefault('You', score)
		f['data'] = data


def displayHighScore():
	data = {}
	with shelve.open('.\\highscores\\highscores') as f:
		data = f['data']
	
	scores = list(data.values())
	scores.sort(reverse=True)
	text = ''

	for score in scores:
		for key in list(data.keys()):
			if data[key] == score:
				text += key + " : " + str(score) + '\n'
	
	return text


#============================= Game Control Panel ==============================#
class ControlPanel():
	def __init__(self, surface):
		self.surface	= surface
		self.width		= width
		self.height		= 80
		self.x 			= 0
		self.y			= height - self.height
		self.config		= (self.x, self.y, self.width, self.height)
		self.color 		= (255, 255, 255)
	

	def draw(self, score, char_health, boss_health=None):
		# control panel surface
		pygame.draw.rect(self.surface, self.color, self.config)

		#instruction label
		ins_x = self.x + 10
		ins_y = self.y + 10
		ins_y2 = self.y + 30
		font = pygame.font.SysFont('comicsans', 25)
		ins1 = font.render('Press Space to shoot', 1, (0, 0, 255))
		ins2 = font.render('Press P to pause', 1, (0, 0, 255))
		self.surface.blit(ins1, (ins_x, ins_y))
		self.surface.blit(ins2, (ins_x, ins_y2))
		
		# health bar
		healthbar_x = self.x + 450
		healthbar_y = self.y + 5
		font = pygame.font.SysFont('comicsans', 25)
		text = font.render('Health: ', 1, (0, 0, 255))
		self.surface.blit(text, (healthbar_x, healthbar_y))
		heart_x = healthbar_x + 100 # x cordinate of the first heart images
		damage = 10 - char_health # the damage taken

		for health in range(char_health): # display all the heart images
			self.surface.blit(health_img, (heart_x, healthbar_y))
			heart_x += 20

		for dam in range(damage):
			self.surface.blit(healthless_img, (heart_x, healthbar_y))
			heart_x += 20

		#score bar
		scorebar_x 	= self.x + 260
		scorebar_y	= self.y + 5
		font2 = pygame.font.SysFont('comicsans', 25)
		text2 = font2.render('Score: ' + str(score), 1, (0, 0, 255))
		self.surface.blit(text2, (scorebar_x, scorebar_y))

		#boss health bar
		if boss_health != None:
			# health bar config
			bhb_x 		= self.x + 240
			bhb_y		= self.y + 40
			bhb_width	= self.width  // 2
			bhb_height	= self.height // 4

			pygame.draw.rect(self.surface, (255, 0, 0), (bhb_x, bhb_y, bhb_width, bhb_height)) # healbar background

			healthbarWidth = bhb_width - ((bhb_width // 20) * (20 - boss_health))
			pygame.draw.rect(self.surface, (0, 255, 0), (bhb_x, bhb_y, healthbarWidth, bhb_height)) 


#============================= Game Character ==============================#
# main character object
class main_character():
	def __init__(self, surface):
		self.surface 	= surface

		# character config
		self.color 		= (255, 0, 0)
		self.x 			= (width // 2 - 64 // 2)
		self.y 			= 300
		self.vel 		= 10
		self.image 		= character_img

		#hitbox
		self.hb_x		= self.x + 7
		self.hb_y		= self.y
		self.hb_width 	= 50
		self.hb_height 	= 64

		# character status
		self.dragging 	= False
		self.health		= 10
		self.won		= False


	def updateHitbox(self):
		self.hb_x		= self.x + 9
		self.hb_y		= self.y
		self.hb_width 	= 45
		self.hb_height 	= 64


	def draw(self):
		self.move()
		self.surface.blit(self.image, (self.x, self.y))
		#pygame.draw.rect(self.surface, self.color, (self.hb_x , self.hb_y, self.hb_width, self.hb_height), 2)

		if self.health <= 0:
			font = pygame.font.SysFont('comicsans', 100)
			text = font.render('You are dead!!', 1, (255, 255, 0))
			self.surface.blit(text, (width // 2 - (text.get_width() // 2), height // 2))
			pygame.display.update()
			pygame.time.delay(1000)
			self.__init__(self.surface)
		
		if self.won:
			font = pygame.font.SysFont('comicsans', 100)
			text = font.render('You won!!', 1, (255, 255, 0))
			self.surface.blit(text, (width // 2 - (text.get_width() // 2), height // 2))
			pygame.display.update()
			pygame.time.delay(1000)
			self.__init__(self.surface)


	def checkForCollison(self, x, y):
		if (self.hb_y < y) and (self.hb_y + self.hb_height > y):
			if (self.hb_x < x) and (self.hb_x + self.hb_width > x):
				return True
		else:
			return False


	def collisonPoints(self):
		return [(self.hb_x, self.hb_y), (self.hb_x, self.hb_y + self.hb_height), 
			    (self.hb_x + self.hb_width, self.hb_y), (self.hb_x + self.hb_width, self.hb_y + self.hb_height)]


	def move(self):
		
		self.updateHitbox()


# enemy object divided by level
class enemyObject():
	def __init__(self, surface):
		self.surface 	= surface
		self.level 		= 1
		self.x 			= random.randrange(50, 700, 80)
		self.y 			= -100
		self.direction 	= random.choice([1, -1])

		# enemy config
		self.color 		= (0, 0, 255)
		self.width 		= 24
		self.height 	= 24
		self.velx 		= random.choice([3, 5]) * self.direction
		self.vely		= random.choice([3, 5])
		self.damage		= 1
		self.images_dir = os.path.join(images_path, 'enemylevel1')
		self.image		= self.getImage()

		#enemy status
		self.dangerous 	= True
		self.score 		= 5


	def getImage(self):
		url = os.path.join(self.images_dir, random.choice(os.listdir(self.images_dir)))
		return pygame.image.load(url)


	def draw(self):
		self.move()
		self.surface.blit(self.image, (self.x, self.y))
		#pygame.draw.rect(self.surface, self.color, (self.x , self.y, self.width, self.height), 2)


	def move(self):
		if self.velx > 0:
			if self.x + self.width + self.velx < width:
				self.x += self.velx
			else:
				self.velx *= -1

		else:
			if self.x + self.velx > 0:
				self.x += self.velx
			else:
				self.velx *= -1

		self.y += self.vely

		if self.y > 420:
			self.dangerous = False


	def checkForCollison(self, x, y):
		if (self.y < y) and (self.y + self.height > y):
			if (self.x < x) and (self.x + self.width > x):
				return True
		else:
			return False


	def collisonPoints(self):
		if self.dangerous:
			return [(self.x, self.y), (self.x, self.y + self.height), 
			    	(self.x + self.width, self.y), (self.x + self.width, self.y + self.height)]
		else:
			return (-10, -10) ,


class enemyObjectL2(enemyObject):
	def __init__(self, surface):
		super().__init__(surface)

		#enemy config
		self.level		= 2
		self.color 		= (123, 0, 255)
		self.width 		= 64
		self.height 	= 64
		self.velx 		= random.choice([4, 7]) * self.direction
		self.vely		= 4
		self.images_dir = os.path.join(images_path, 'enemylevel2')
		self.image		= self.getImage()
		self.damage		= 2
		self.score		= 10

		
class enemyObjectL3(enemyObject):
	def __init__(self, surface):
		super().__init__(surface)

		#enemy config
		self.x 			= random.choice([50, 200, 300, 500])
		self.y			= -200
		self.level		= 3
		self.color 		= (123, 100, 255)
		self.width 		= 128
		self.height 	= 128
		self.velx 		= random.choice([1, 2]) * self.direction
		self.vely		= 1
		self.images_dir = os.path.join(images_path, 'enemylevel3') 
		self.image		= self.getImage()
		self.damage		= 4
		self.score		= 20


class projectiles(enemyObject):
		def __init__(self, surface, x, y, direction):
			super().__init__(surface)
			self.x 			= x
			self.y 			= y
			self.direction 	= direction


class enemyObjectBoss(enemyObject):
	def __init__(self, surface):
		super().__init__(surface)

		#enenmy config
		self.level 					= 100
		self.width 					= 256
		self.height 				= 256
		self.x 						= (width // 2) - (self.width // 2)
		self.y						= -300
		self.velx					= 0
		self.vely					= 1
		self.damage    				= 10
		self.images_dir 			= os.path.join(images_path, 'boss')
		self.image					= self.getImage()
		self.health					= 20
		self.score					= 100
		self.projectiles_contain	= []


	def move(self):
		i = 0
		while i < 10000:
			i += 0.1
		super().move()
	


# bullet object
class bulletsObject(enemyObject):
	def __init__(self, surface, x, y):
		self.surface 	= surface
		self.x 			= x
		self.y 			= y
		self.width 		= 32
		self.height		= 32
		self.image 		= pygame.image.load(images_path + '\\missile.png')

		self.visible	= True
	

	def move(self):
		if self.visible:
			if self.y + self.width > 0:
				self.y -= 2
			else:
				self.visible = False
	

	def draw(self):
		if self.visible:
			self.move()
			self.surface.blit(self.image, (self.x, self.y))
			#pygame.draw.rect(self.surface, (255, 0, 0), (self.x , self.y, self.width, self.height), 2)


	def collisonPoints(self):
		if self.visible:
			return [(self.x, self.y), (self.x, self.y + self.height), 
			    	(self.x + self.width, self.y), (self.x + self.width, self.y + self.height)]
		else:
			return (-550, -50) ,


def main():
	'''
		Main fuction to run the game
	'''

	# game setting
	pygame.init()
	pygame.display.set_caption(game_title)
	screen 			= pygame.display.set_mode((width, height))
	clock 			= pygame.time.Clock()
	score 			= 0
	level 			= 1
	randomCreation 	= 1
	pause 			= False
	CONTROL_PANEL   = ControlPanel(screen)

	# creating character
	ufo = main_character(screen)

	#enemy management
	list_of_enemies 	= []
	ene_l3 = 0
	boss_health = None

	#bullet management
	bullets = []
	shootLoop = 0

	running = True

	def redrawScreen(boss_health):
		'''
			Function to update screen
		'''
		# update ufo 
		ufo.draw()

		#update bullets
		for bullet in bullets:
			bullet.draw()

		#update enemy
		for enemy in list_of_enemies:
			enemy.draw()
			if enemy.level == 100:
				boss_health = enemy.health

		# update the screen
		CONTROL_PANEL.draw(score, ufo.health, boss_health)
		pygame.display.update()
		screen.fill((0, 128, 128))

	
	while running:
		dt = clock.tick(60)

		# delay shooting bullets
		if shootLoop > 0:
			shootLoop += 1
		if shootLoop > 10:
			shootLoop = 0

		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					ufo.dragging = False
					pause = not pause
			# check for dragging
			elif not pause:
				if event.type == pygame.MOUSEBUTTONDOWN: #check for click a mouse button
					if event.button == 1: #check if it was a right mouse click
						mouse_x, mouse_y = event.pos
						if ufo.checkForCollison(mouse_x, mouse_y): #check if the mouse was cliked on
							ufo.dragging = True
							offset_x = ufo.x - mouse_x
							offset_y = ufo.y - mouse_y

				elif event.type == pygame.MOUSEBUTTONUP: #check if the mouse was released
					if event.button == 1:
						ufo.dragging = False

				elif event.type == pygame.MOUSEMOTION: #check for the mouse position when dragging it
					if ufo.dragging:
						mouse_x, mouse_y = event.pos
						
						if mouse_x + ufo.hb_width > width:
							mouse_x = width - ufo.hb_width

						if mouse_y > CONTROL_PANEL.y:
							mouse_y = CONTROL_PANEL.y - ufo.hb_height + 40
						ufo.x = mouse_x + offset_x
						ufo.y = mouse_y + offset_y
		
		if pause:
			continue

		#setting the bullets
		for bullet in bullets:
			if bullet.visible:
				bullet.move()
			else:
				bullets.pop(bullets.index(bullet))
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and shootLoop == 0:
			if len(bullets) < 3:
				bullets.append(bulletsObject(screen, ufo.x, ufo.y))
			shootLoop = 1
		

		#setting up the enemies
		if level == 1:
			if len(list_of_enemies) < 7:
				list_of_enemies.append(enemyObject(screen))
		elif level == 2:
			randomCreation = random.choice([1, 2])

			if len(list_of_enemies) < 10:
				if randomCreation == 1:
					list_of_enemies.append(enemyObject(screen))
				else:
					list_of_enemies.append(enemyObjectL2(screen))
		elif level == 3:
			max_of_level3 = random.choice([1, 2, 2])
			if ene_l3 < max_of_level3 and len(list_of_enemies) < 7:
				list_of_enemies.append(enemyObjectL3(screen))
				ene_l3 += 1
			else:
				randomCreation = random.choice([1, 2, 2])

				if len(list_of_enemies) < 7:
					if randomCreation == 1:
						list_of_enemies.append(enemyObject(screen))
					else:
						list_of_enemies.append(enemyObjectL2(screen))
		else:
			if len(list_of_enemies) == 0:
				list_of_enemies.append(enemyObjectBoss(screen))
			
			for enemy in list_of_enemies:
				if enemy.level == 100 and len(list_of_enemies) < 5:
					boss 		= enemy
					kid1		= projectiles(screen, boss.x, boss.y + boss.height, -1)
					kid2		= projectiles(screen, boss.x + 30, boss.y + boss.height, -1)
					kid3		= projectiles(screen, boss.x + 100, boss.y + boss.height, 1)
					kid4		= projectiles(screen, boss.x + 170, boss.y + boss.height, 1)
					list_of_enemies.append(kid1)
					list_of_enemies.append(kid2)
					list_of_enemies.append(kid3)
					list_of_enemies.append(kid4)
		for enemy in list_of_enemies:
			if not enemy.dangerous:
				score += enemy.score
				list_of_enemies.pop(list_of_enemies.index(enemy))
				
				if enemy.level == 3:
					ene_l3 -= 1
	
		#check for collisons
		for enemy in list_of_enemies:
			if enemy.width <= ufo.hb_width:	
				for point in enemy.collisonPoints():
					x, y = point
					if ufo.checkForCollison(x, y):
						ufo.health -= enemy.damage
						enemy.dangerous = False
						break
			else:
				for point in ufo.collisonPoints():
					x, y = point
					if enemy.checkForCollison(x, y):
						ufo.health -= enemy.damage
						enemy.dangerous = False
						break
			
			for bullet in bullets:
				for point in bullet.collisonPoints():
					x, y = point
					if enemy.checkForCollison(x, y):
						if enemy.level == 100:
							enemy.health -= 1
							if enemy.health <= 0:
								ufo.won = True
								enemy.dangerous = False
						else:
							enemy.dangerous = False
						bullet.visible 	= False
						break
		
		#reset game
		if ufo.health <= 0 or ufo.won:
			saveTheScore(score)
			list_of_enemies = []
			score = 0
			level = 1
			randomCreation = 1

		#set the level
		if score > 150:
			level = 2
		if score > 200:
			level = 3
		if score > 700:
			level = 100
		redrawScreen(boss_health)

main()

#print(displayHighScore())