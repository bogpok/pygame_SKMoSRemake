import pygame as pg
from helper import load_image
from classes import *

N = 4
WINDOWSIZE = (240*4, 160*4) # GBA is 240x160

yoh = {
	"idle":"../assets/yoh/idle/idle1_29x41.png"
}

paths = {
	"yoh":yoh
}

def main():
	# inits
	pg.init()
	screen = pg.display.set_mode(WINDOWSIZE)
	clock = pg.time.Clock()

	# load sprites

	yoh = Character((100,100),(50,50),load_image(paths["yoh"]["idle"])[0])

	

	running = True
	while running:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False


		yoh.draw(screen)
		pg.display.flip()

	pg.quit()





if __name__ == "__main__":
	main()
