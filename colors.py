import random as r

class Colors():
	aqua = (0,255,255)
	black = (0,0,0)
	blue = (0,0,255)
	brown = (128,0,0)
	darkBlue = (0,0,128)
	diamond = (0,128,128)
	gold = (255,215,0)
	gray = (128,128,128)
	green = (0,128,0)
	haki = (240,230,140)
	lime = (0,255,0)
	olive = (128,128,0)
	orange = (255,165,0)
	pink = (255,0,255)
	purple = (128,0,128)
	red = (255,0,0)
	silver = (192,192,192)
	white = (255,255,255)
	yellow = (255,255,0)
	def getRandom():
		random = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
		return random
