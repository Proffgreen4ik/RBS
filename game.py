import pygame as p 
import colors as c

class Game():
	leftDeaths = 0
	rightDeaths = 0
	team1 = []
	team2 = []
	weapons = []
	allobj = []
	dWidth = 1920
	dHeight = 1080
	count = 60
	leftColor = c.Colors.getRandom()
	rightColor = c.Colors.getRandom()
	feelings = False
	#friendlyFire = True
	win = p.display.set_mode((dWidth,dHeight))