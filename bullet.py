import game as g
import pygame as p 
import random as r

class Bullet():
	def __init__(self): 
		self.size = 1 
		self.x = 0
		self.y = 0
		self.ry1 = 0
	
	def draw(self,color,vector,speed,damage,recoil,x,y):
		if vector == "right":
			mas = g.Game.team2
		elif vector == "left":
			mas = g.Game.team1
		for i in range (len(mas)):
			self.y += self.ry1 
			if vector == "right":
				self.x += speed 
			elif vector == "left":
				self.x -= speed 
			p.draw.circle(g.Game.win,color,[self.x,self.y],self.size) 
			if self.x >= g.Game.dWidth or self.x == 0 or self.x <= 0:
				self.y = y
				self.x = x
				self.ry1 = r.uniform(-recoil,recoil)
			elif (self.x <= mas[i].x+mas[i].size and self.x >= mas[i].x-mas[i].size and self.y <= (mas[i].y+mas[i].size) and self.y >= (mas[i].y-mas[i].size)) or (self.x >= mas[i].x-mas[i].size and self.x<=mas[i].x+mas[i].size and self.y <= (mas[i].y+mas[i].size) and self.y >= (mas[i].y-mas[i].size)):
				if mas[i].health > 0:
					if mas[i].armor > 0:
						mas[i].health -= damage/(mas[i].armor/10)
						mas[i].armor -= damage/10
						if vector == "right":
							print('Левый попал, урон:',damage,'Здоровье правого:',mas[i].health,'Броня правого:',mas[i].armor) 
						elif vector == "left":
							print('Правый попал, урон:',damage,'Здоровье левого:',mas[i].health,'Броня левого:',mas[i].armor) 
					else:
						mas[i].health -= damage
			