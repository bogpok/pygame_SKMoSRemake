import pygame as pg
class Character:
	def __init__(self, xy0, wh, image):
		
		self.image = image
		self.rect = image.get_rect(bottomleft = xy0)
		self.speed = 10

		self.dx = 0

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def runs(self, direction):
		self.dx = direction
		print(self.dx)

	def move(self):
		self.rect.x = self.rect.x + self.dx * self.speed
		