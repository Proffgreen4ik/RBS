import pygame as p 
import game as g
import colors as c

p.init()  
f1 = p.font.Font(None,54) 

def endGame():
	if len(g.Game.team1) == g.Game.leftDeaths or len(g.Game.team2) == g.Game.rightDeaths:
		g.Game.win.fill(c.Colors.black)	
		if len(g.Game.team1) == g.Game.leftDeaths:
			g.Game.win.blit(f1.render("Победа правых",True,g.Game.rightColor),(g.Game.dWidth/2-150,g.Game.dHeight/2))
		else:
			g.Game.win.blit(f1.render("Победа левых",True,g.Game.leftColor),(g.Game.dWidth/2-150,g.Game.dHeight/2))
		p.mixer.music.stop()

		