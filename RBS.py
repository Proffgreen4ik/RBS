########################################################V 1.0.2 Нормальная графика и фикс отъема hp 
########################################################V 1.0.3 Добавление механики брони и винтовки, после смерти игрок перестает стрелять
########################################################V 1.0.4 Алгоритм рандомного спауна с рандомным оружием и выстрелов в соответствии, 
#																изоляция вектора от оружия и присвоение вектора герою, 
#                                                               создание массива оружия, передвижение игрока в пределах локации
########################################################V 1.0.5 Разные алгоритмы полета пуль для разного типа оружия, добавление разброса
########################################################V 1.0.6 Общая оптимизация, оповещение о победе какой-либо из команд, оптимизация патронов и оружия, 
#                                                               полноэкранный режим, добавление новых цветов героев, модульная структура                                                
########################################################V 1.0.7 Оптимизация модулей, другая механика брони
########################################################V 1.0.8 Добавление пулемета и револьвера
#V 1.0.9 friendly fire, добавление чувств(философская отсылка), добавление статистики (киллы,броня,здоровье,оружие)
#V 1.1.1 Добавление deagle,m4a4,shotgun, добавление локаций и новых команд, фикс отъема хп
#V 1.1.2 Добавление уровней в зависимости от киллов
#V 1.1.3 Выбор цвета и количества игроков в команде

#Поключеие библиотек
import pygame as p 
import random as r
import colors as c
import hero as h
import weapon as w
import functions as f
import game as g

p.display.set_caption("REAL BATTLE SIMULATOR v 1.0.8") 
p.mixer.music.load('fon_muse.mp3')
p.mixer.music.play()
#locLeft = [0,dWidth/2]
#locRight = [dWidth/2,dWidth]

for i in range(g.Game.count):
	if i < g.Game.count/2:
		g.Game.allobj.append(h.Hero(g.Game.leftColor,"right"))
	else:
		g.Game.allobj.append(h.Hero(g.Game.rightColor,"left"))
		
for i in range(len(g.Game.allobj)):
	if i < len(g.Game.allobj)/2: 
		g.Game.team1.append(g.Game.allobj[i])
	else:
		g.Game.team2.append(g.Game.allobj[i])

while True: 
	g.Game.win.fill(c.Colors.black)	
	for i in range(len(g.Game.allobj)):
		g.Game.allobj[i].draw()
		if (g.Game.allobj[i].health > 0):
			g.Game.allobj[i].attack()
			g.Game.allobj[i].moveControl()
		g.Game.allobj[i].isAlive()
	f.endGame()
	p.display.update()

