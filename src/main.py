import pygame as pg
from helper import load_image, load_json
from classes import *

N = 2
WINDOWSIZE = (240*N, 160*N) # GBA is 240x160

yoh = {
	"idle":"../assets/yoh/idle/idle1_29x41.png"
}

paths = {
	"yoh":yoh
}


def load_globals():
	config = load_json("./config.json")	
	global GLP, YSP, FPS
	GLP = WINDOWSIZE[1]-WINDOWSIZE[1]*config['groundLevelPercents']
	YSP = WINDOWSIZE[1]*config['yohSizePercent']
	FPS = 60


def main():
	load_globals()	
	# inits
	pg.init()
	screen = pg.display.set_mode(WINDOWSIZE)
	clock = pg.time.Clock()

	# load sprites

	yoh = Character((100,GLP),(50,50),load_image(paths["yoh"]["idle"], scale=round(YSP/41))[0])

	

	running = True
	while running:
		clock.tick(FPS)
		screen.fill("green")
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_d:
					yoh.runs(1)
				elif event.key == pg.K_a:
					yoh.runs(-1)
					print("wtf")
			if event.type == pg.KEYUP:
				yoh.runs(0)


		yoh.move()
		yoh.draw(screen)
		pg.display.flip()

	pg.quit()





if __name__ == "__main__":
	main()
