import bullet as b
import random as r
import game as g

class Weapon():
	def __init__(self, name, speed, damage,recoil):
		self.name = name 
		self.bullet = b.Bullet() 
		self.speed = speed
		self.damage = damage
		self.recoil = recoil

	def shoot(self,color,vector,speed,damage,recoil,x,y):
		self.bullet.draw(color,vector,speed,damage,recoil,x,y)

	def getAK47(self):
		return Weapon("AK47",3,120,0.45)

	def getUSP(self):
		return Weapon("USP",0.7,50,0.2)

	def getAWP(self):
		return Weapon("AWP",0.25,1000,0.01)

	def getRevolver(self):
		return Weapon("REVOLVER",0.4,500,0.6)

	def getMinigun(self):
		return Weapon("MINIGUN",5,100,0.8)

	def getRandom(self):
		wp = r.choice(['AWP','AK47','USP','REVOLVER','MINIGUN'])
		if wp == 'AWP':
			return Weapon.getAWP(self)
		elif wp == 'AK47':
			return Weapon.getAK47(self)
		elif wp == "REVOLVER":
			return Weapon.getRevolver(self)
		elif wp == "MINIGUN":
			return Weapon.getMinigun(self)
		else:
			return Weapon.getUSP(self)