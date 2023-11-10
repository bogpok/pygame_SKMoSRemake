import pygame as pg
class Character:
	def __init__(self, xy0, wh, image):
		self.rect = pg.Rect(xy0, wh)
		self.image = image

	def draw(self, screen):
		screen.blit(self.image, self.rect)
