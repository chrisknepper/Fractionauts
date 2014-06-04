from  SceneBasic import *
import DrawHelper
import HelperVec2
import random
from IcnBasic import IcnBasic 
from IcnParticleShootingStar import IcnParticleShootingStar 
from IcnParticleDistortCustomRange import IcnParticleDistortCustomRange

import SoundManager

class SceneMenu(SceneBasic):	
	def __init__(self,  resolution):
		SceneBasic.__init__(self,resolution)

	
	def registerEvent_play(s,e): s.EVENT_PLAY.append(e); pass
	def registerEvent_help(s,e):s.EVENT_HELP.append(e);pass
	def registerEvent_quit(s,e):s.EVENT_QUIT.append(e);pass

	def initEvents(s):
		s.EVENT_PLAY = [ ];
		s.EVENT_HELP = [ ];
		s.EVENT_QUIT = [ ];

	def initImages(s,resolution):
		#s.textureIdTitle =	TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png'), HelperVec2.mult(resolution, (.7,.13)))
		s.textureIdTitle =	TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png') )
		s.textureIdBG =		TextureLoader.load(os.path.join('assets', 'screenStart', 'background.png') ,resolution);

		s.textureIdBttnStart = 	TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnStart.png') );
		s.textureIdBttnHelp = 	TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnHelp.png') );
		s.textureIdBttnExit = 	TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnExit.png') );

		s.textureIdShootingStar_00 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar00.png') );
		s.textureIdShootingStar_01 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar01.png') );
	
	def initOthers(s , resolution):
		s.initParticles(resolution)
		s.renderScreenObjects.extend(s.arrShootingStars)

		s.icnMouse = IcnBasic.FROM_PATH(os.path.join('assets', 'screenCommon', 'cursor.png') )
		s.renderScreenObjects.append(s.icnMouse)

	def helperInitKButton(s, center, textureID):
		texture = TextureLoader.get( textureID)
		size = (texture.get_width(),texture.get_height())
		return KButton(center[0] -size[0] *.5,center[1]-size[1]*.5,size[0],size[1], textureID )

	def initButtons(s,resolution):
		center = HelperVec2.mult(resolution, (.5,.5) ) 
		# Main menu buttons
		s.bttnPlay =	s.helperInitKButton ((center[0],center[1]-60),s.textureIdBttnStart)# KButton(center[0]-100, center[1] - 100, 200, 75,s.textureIdBttnStart)
		s.bttnHow =	s.helperInitKButton ((center[0],center[1]), s.textureIdBttnHelp) 
		s.bttnQuit =	s.helperInitKButton ((center[0],center[1]+60), s.textureIdBttnExit)  #KButton(center[0]  -100,center[1] + 100, 200, 75,s.textureIdBttnExit)

		s.buttons = [s.bttnPlay,s.bttnHow,s.bttnQuit]

	def initParticles(s,resolution):
		s.arrShootingStars = []
		s.distortH = IcnParticleDistortCustomRange(0,80,resolution[0],5/600.0 * resolution[1], s.myBackground,1,0 )
		s.distortV = IcnParticleDistortCustomRange(100, 0,resolution[0],2/600.0 * resolution[1], s.myBackground,-1,0 )
		s.distortSpacing = 5/600.0 * resolution[1]  *.5
		s.arrShootingStars.append(s.distortH)
		s.arrShootingStars.append(s.distortV)

		for i in range(0, 3):
			textureId = s.textureIdShootingStar_00 if random.random() <.5\
					else  s.textureIdShootingStar_01
			texture = TextureLoader.get(textureId)
			size = (texture.get_width() , texture.get_height() )
			p = IcnParticleShootingStar( random.random()  * resolution[0] ,random.random()  * -resolution[1],size[0],size[1],textureId,resolution)
			s.arrShootingStars.append(p)
		#s.distortH = IcnParticleDistortCustomRange(0,80,resolution[0],15, s.myBackground,1,0 )
		#s.distortV = IcnParticleDistortCustomRange(100, 0,15,resolution[1], s.myBackground,1,0 )
		

		pass
	def EVENT_SCENE_START(self):
		print("SCENE_BASIC_ENTER")
		IcnParticleShootingStar.textureBG = self.myBackground

	def EVENT_CLICK(self):
		mouseAt = pygame.mouse.get_pos();
		buttons_event = [
					[self.bttnQuit ,self.EVENT_QUIT],
					[self.bttnPlay , self.EVENT_PLAY],
					[self.bttnHow ,self.EVENT_HELP],
				]

		for bttn,event in buttons_event:
			if bttn.isUnder(mouseAt):
				self.helperRaiseEvent(event)
				break

	def initBackground(s,screen,size):
		screen.fill((255, 255, 255)) 
		DrawHelper.drawAspect(screen, s.textureIdBG,0,0)
		DrawHelper.drawAspect(screen, s.textureIdTitle,.12,.1)
		for button in s.buttons: button.draw(screen)
	
	ratio = 0
	def renderUpdate(s,timeElapsed):
		s.icnMouse.pos =  pygame.mouse.get_pos()
		s.ratio = (s.ratio+800.15*timeElapsed ) % 3.5
		s.distortH.range = (s.ratio ,s.ratio)
		s.distortV.range = (-s.ratio , -s.ratio)
		#s.distortH.pos = (0,pygame.mouse.get_pos()[1]) 
		#s.distortV.pos = (pygame.mouse.get_pos()[0],0) 
		s.distortH.pos =(0, pygame.mouse.get_pos()[1])
		s.distortV.pos = (0,pygame.mouse.get_pos()[1]+s.distortSpacing )
		for icn in s.arrShootingStars:
			icn.drawUpdate(timeElapsed)




#def initButtons(s,resolution):
		#remove all the shit below fuck
		#Load in Title Image and background images
	#	
	#	s.logo = s.helperLoadImage(os.path.join('assets', 'startscreen', 'Title.png'))
	#	s.startbg = s.helperLoadImage(os.path.join('assets', 'startscreen', 'night_sunset_gradient.png'))
	#	s.startbg = s.helperRescaleImage(s.startbg ,(800,600) )
	#	
	#	#idiotic scrollingImage take care of it please 
	#	s.stars_tiny =  ScrollingImage( \
	#					   pygame.image.load(os.path.join('assets', 'startscreen', \
	#									   'stars_tiny.png')), (-50,-50), float(.004))
	#	s.stars_small = ScrollingImage( \
	#					   pygame.image.load(os.path.join('assets', 'startscreen', \
	#									   'stars_small.png')), (-50,-50), float(.008))
	#	s.stars_medium = ScrollingImage( \
	#						pygame.image.load(os.path.join('assets', 'startscreen', \
	#									   'stars_medium.png')), (-50,-50), float(.012))
	#	s.stars_big = ScrollingImage( 
	#		s.helperLoadImage(os.path.join('assets', 'startscreen', 'stars_big.png')) \
	#		, (-50,-50), float(.36))
		#idiot idiot stupid 
	#	s.sunsetoverlay = pygame.image.load(os.path.join('assets', 'startscreen', 'sunset_overlay.png'))



#def renderScreen(s, screen):
#s.main.screen.blit(s.startbg, (0, 0))
		#self.stars_tiny.draw(self.main.screen,tick) ;
		#self.stars_small.draw(self.main.screen, tick);
		#self.stars_medium.draw(self.main.screen,tick);
		#self.stars_big.draw(self.main.screen, tick);
		
		#self.main.screen.blit(self.sunsetoverlay, (0, 0)) # this might make it too dim
	 	 # self.main.screen.blit(self.logo, (self.main.hcenter - 300, 150))



# woooha no please

#	def helperLoadImage(self, osPath):
#		img = pygame.image.load(osPath).convert_alpha();
#		return img
#	def helperRescaleImage(self, img, scale):
#		return pygame.transform.scale(img, scale)
#	def helperLoadImageAsScrolling(self, osPath, A, B):
#		return pygame.image.load(osPath)	