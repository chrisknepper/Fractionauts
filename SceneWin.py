import pygame
import os

import TextureLoader
import DrawHelper
 
from SceneBasic import SceneBasic

class SceneWin(SceneBasic):
	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)
		pass

	def initImages(s,screenSize):
		s.textureIdBG = TextureLoader.load(os.path.join('assets', 'screenWin', 'win00.png'))
		pass;
	def initEvents(s):
		EVENT_FINISHED = []

	def renderScreenBegin(s,screen):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0)
		pygame.display.update()
		pass
	def renderScreen(s,Screen):
		pass

