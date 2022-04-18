import pygame as p 
import colors as c
import game as g
import weapon as w
import random as r

class Hero():
	def __init__(self, color, vector):
		self.color = color
		self.size = 7 
		self.weapon = w.Weapon.getRandom(self) 
		self.health = 100  
		self.armor = 100
		self.vector = vector 
		self.notDeath = True
		self.speed = 2.5
		if self.vector == "right":
			self.x = r.randint(30,g.Game.dWidth/2)
		elif self.vector == "left":
			self.x = r.randint(g.Game.dWidth/2+10,g.Game.dWidth-40)
		self.y = r.randint(20,g.Game.dHeight-50)

	def attack(self):
		if g.Game.feelings == False:
			self.weapon.shoot(self.color,self.vector,self.weapon.speed,self.weapon.damage,self.weapon.recoil,self.x,self.y)

	def moveControl(self):
		if self.vector == "left" or self.vector == "right":
			if (self.x >= g.Game.dWidth/2+10 and self.x <= g.Game.dWidth-40 and self.y>=50 and self.y<=g.Game.dHeight-50) or (self.x >=30 and self.x <= g.Game.dWidth/2 and self.y>=50 and self.y<=g.Game.dHeight-50):
				self.x += r.uniform(-self.speed,self.speed)
				self.y += r.uniform(-self.speed,self.speed)
			else:
				if self.vector == "left":
					self.x = r.randint(g.Game.dWidth/2+10,g.Game.dWidth-40)
				else:
					self.x = r.randint(30,g.Game.dWidth/2)
				self.y = r.randint(20,g.Game.dHeight-50)

				
	def isAlive(self): 
		if self.notDeath == True:
			if self.health <= 0:
				self.color = c.Colors.white 
				self.notDeath = False 
				if self.vector == "left":
					g.Game.rightDeaths += 1
				else:
					g.Game.leftDeaths += 1 

	def draw(self):
		p.draw.circle(g.Game.win,self.color,[self.x,self.y],self.size) 