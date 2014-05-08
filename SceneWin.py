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

	def registerEvent_finished(s,event): s.EVENT_FINISHED.append(event)
	def initEvents(s):
		s.EVENT_FINISHED = []

	def EVENT_CLICK(s):
		s.helperRaiseEvent(s.EVENT_FINISHED)

	def renderScreenBegin(s,screen):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0)
		pygame.display.update()
		pass
	def renderScreen(s,Screen):
		pass

