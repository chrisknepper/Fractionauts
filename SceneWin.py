import pygame
import os

import TextureLoader
import DrawHelper
 
from SceneBasic import SceneBasic

class SceneWin(SceneBasic):
	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)
		self.time = 0;
		pass

	def initImages(s,screenSize):
		s.textureIdBG = TextureLoader.load(os.path.join('assets', 'screenWin', 'win00.png'))
		pass;

	def registerEvent_finished(s,event): s.EVENT_FINISHED.append(event)
	def initEvents(s):
		s.EVENT_FINISHED = []

	def EVENT_CLICK(s):
		s.helperRaiseEvent(s.EVENT_FINISHED)

	def EVENT_SCENE_START(s):
		s.time = 0

	def renderScreenBegin(s,screen):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0)
		pygame.display.update()
		pass
	def renderScreen(s,Screen):
		pass

	def renderUpdate(s, timeElapsed):
		s.time += timeElapsed
		if(s.time > 10) :  
			print "Next frame now"
			s.helperRaiseEvent(s.EVENT_FINISHED)
		pass

