from  SceneBasic import *
import DrawHelper

class SceneGameMenu(SceneBasic):	
	def __init__(self, main,  resolution):
		SceneBasic.__init__(self,main,resolution)

	

	def initEvents(s):
		s.EVENT_PLAY = [ ];
		s.EVENT_TUTORIAL = [ ];
		s.EVENT_QUIT = [ ];

		def ME_EVENT_PLAY(): s.main.set_mode('play'); pass
		def ME_EVENT_TUTORIAL():s.main.set_mode('help');pass
		def ME_EVENT_QUIT():
			s.main.saveLevel()
			s.running = False
			pygame.quit()
			exit()
			pass

		s.EVENT_PLAY.append(ME_EVENT_PLAY)
		s.EVENT_TUTORIAL.append(ME_EVENT_TUTORIAL)
		s.EVENT_QUIT.append(ME_EVENT_QUIT)

	def initImages(s,resolution):
		s.textureIdLogo =	TextureLoader.load(os.path.join('assets', 'startscreen', 'Title.png'));
		s.textureIdBG =		TextureLoader.load(os.path.join('assets', 'startscreen', 'night_sunset_gradient.png') ,scale = resolution);
		s.textureIdBG_sunsetoverlay = TextureLoader.load(os.path.join('assets', 'startscreen', 'stars_big.png') );

		s.textureIdStarTiny =  	TextureLoader.load(os.path.join('assets', 'startscreen', 'stars_tiny.png')) ;
		s.textureIdStarSmall= 	TextureLoader.load(os.path.join('assets', 'startscreen', 'stars_small.png')) ;
		s.textureIdStarMedium= TextureLoader.load(os.path.join('assets', 'startscreen', 'stars_medium.png')) ;
		s.textureIdStarBig = 	TextureLoader.load(os.path.join('assets', 'startscreen', 'stars_big.png')) ;
		
	def initButtons(s,resolution):
		center = (resolution[0] *.5,resolution[1]*.5);
		# Main menu buttons
		s.bttnPlay =	Button( center[0]- (75 * 1.5),center[1] - 100, 200, 75, 'Play')
		s.bttnHow =	Button(center[0] - (75 * 1.5),center[1], 200, 75, 'How to Play')
		s.bttnQuit =	Button(center[0]  - (75 * 1.5),center[1] + 100, 200, 75, 'Quit')

		s.buttons = []
		s.buttons.append(s.bttnPlay)
		s.buttons.append(s.bttnHow)
		s.buttons.append(s.bttnQuit)

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

	

	def listenForEvents(self):
		buttons_event = [
					[self.bttnQuit ,self.EVENT_QUIT],
					[self.bttnPlay , self.EVENT_PLAY],
					[self.bttnHow ,self.EVENT_TUTORIAL]
				]

		if 1 in pygame.mouse.get_pressed():
			#Menu state buttons
			mouseAt = pygame.mouse.get_pos();
			for bttn,event in buttons_event:
				if bttn.is_under(mouseAt):
					print 'You clicked the ' + bttn.text + ' button'
					for e in event : e();
					break

	def renderScreen(s, screen):
		DrawHelper.drawAspect(screen, s.textureIdBG, 0,0)
		DrawHelper.drawAspect(screen, s.textureIdBG_sunsetoverlay, 0,0)
		tick = pygame.time.get_ticks()
		for button in s.buttons:
			button.draw(screen)


		
		#s.main.screen.blit(s.startbg, (0, 0))
		#self.stars_tiny.draw(self.main.screen,tick) ;
		#self.stars_small.draw(self.main.screen, tick);
		#self.stars_medium.draw(self.main.screen,tick);
		#self.stars_big.draw(self.main.screen, tick);
		
		#self.main.screen.blit(self.sunsetoverlay, (0, 0)) # this might make it too dim
	 	 # self.main.screen.blit(self.logo, (self.main.hcenter - 300, 150))

	def enter(self):
		print("entered main menu")


# woooha no please

#	def helperLoadImage(self, osPath):
#		img = pygame.image.load(osPath).convert_alpha();
#		return img
#	def helperRescaleImage(self, img, scale):
#		return pygame.transform.scale(img, scale)
#	def helperLoadImageAsScrolling(self, osPath, A, B):
#		return pygame.image.load(osPath)	