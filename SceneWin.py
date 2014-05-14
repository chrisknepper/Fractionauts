import pygame
import os
import math

import TextureLoader
import DrawHelper
import HelperVec2
 
from SceneBasic import SceneBasic
from IcnParticleShootingStar import IcnParticleShootingStar
from IcnBasic  import IcnBasic

class SceneWin(SceneBasic):
	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)
		pass

	def initImages(s,screenSize):
		s.textureIdBG 		= TextureLoader.load(os.path.join('assets', 'screenWin', 'bg.png'))
		s.textureIdRocket 	= TextureLoader.load(os.path.join('assets', 'screenWin', 'rocketFlying.png'))
		pass;

	def registerEvent_finished(s,event): s.EVENT_FINISHED.append(event)
	def initEvents(s):
		s.EVENT_FINISHED = []
	def initOthers(s,screenSize):
		s.time = 0;
		t =  TextureLoader.get(s.textureIdRocket) 
		size =(t.get_width(), t.get_height())
		s.posInit = (screenSize[0]*.5-size[0]*.5+ 10 , screenSize[1]-size[1] +10)
		s.icnRocket = IcnBasic(s.posInit[0],s.posInit[1], size[0],size[1], s.textureIdRocket	)

		textureIdStar00 		= TextureLoader.load(os.path.join('assets', 'screenCommon', 'fast-star01.png'))
		textureIdStar01		= TextureLoader.load(os.path.join('assets', 'screenCommon', 'fast-star02.png'))
		tt = TextureLoader.get(textureIdStar00) 
		sizeStar = (tt.get_width(),tt.get_height())
		s.icnParticleStars = []
		for i in range(0, 20):

			s.icnParticleStars.append(IcnParticleShootingStar(500,-1000,sizeStar[0],sizeStar[1] ,textureIdStar00 , screenSize,( 0,100/600.0 * screenSize[1]) ) )
			s.icnParticleStars.append(IcnParticleShootingStar(500,-10000,sizeStar[0],sizeStar[1] ,textureIdStar01 , screenSize, (0,350/600.0 * screenSize[1]))) 
		s.renderScreenObjects.extend(s.icnParticleStars)
		s.renderScreenObjects.append(s.icnRocket)

	def EVENT_CLICK(s):
		print "SceneWin Click"
		s.helperRaiseEvent(s.EVENT_FINISHED)

	def EVENT_SCENE_START(s):
		s.time = 0

	def initBackground(s,screen,resolution):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0)
		pygame.display.update()
		pass
	def renderScreen(s,screen):
		SceneBasic.renderScreen(s,screen)
		#for e in s.icnParticleStars : 	
		#	s.myBackground.blit(e.mySurface,e.pos )
		#	pygame.display.update( e.draw(screen))


	def renderUpdate(s, timeElapsed):
		s.time += timeElapsed
		move = (math.cos(20*s.time)*10,math.sin(20*s.time) *10)
		s.icnRocket.pos = HelperVec2.add(s.posInit , (move) )
		for e in s.icnParticleStars : e.drawUpdate(timeElapsed)
		if(s.time > 10) :  
			print "Next frame now"
			s.helperRaiseEvent(s.EVENT_FINISHED)
		pass

