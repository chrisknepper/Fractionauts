from  SceneBasic import *
import DrawHelper
import HelperVec2
from IcnBasic import IcnBasic 
from IcnTextBox import IcnTextBox

class SceneHelp(SceneBasic):

	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)

	def initOthers(self, screenSize):
		self.initImages(screenSize)
		self.initIcnText(screenSize)
		self.initButtons(screenSize)

		self.icnMouse = IcnBasic.FROM_PATH(os.path.join('assets', 'screenCommon', 'cursor.png') )
		self.renderScreenObjects.append(self.icnMouse)
	
	def initImages(s,screenSize):
		s.textureIdBG = TextureLoader.load( os.path.join('assets', 'screenStart','background.png'),screenSize)

	def initIcnText(s,screenSize):
		s.icnTextHelp1 = IcnTextBox(100.0/800.0*screenSize[0],150.0/600.0*screenSize[1], 600.0/800.0*screenSize[0],50.0/600.0*screenSize[1], "HOW TO PLAY")
		s.icnTextHelp2 = IcnTextBox(100.0/800.0*screenSize[0],250.0/600.0*screenSize[1], 600.0/800.0*screenSize[0],50.0/600.0*screenSize[1], "FILL THE ROCKET TO SPECIFIED FRACTIONS AND LAUNCH!")
		s.icnTextHelp3 = IcnTextBox(100.0/800.0*screenSize[0],300.0/600.0*screenSize[1], 600.0/800.0*screenSize[0],50.0/600.0*screenSize[1], "CLICK ON FUELS TO FILL THE ROCKET, FUELS CAN BE ADDED UP.")
		s.arrIcnText = [s.icnTextHelp1, s.icnTextHelp2, s.icnTextHelp3]
		pass

	def initButtons(s,screenSize):
		size = HelperVec2.mult(screenSize, (.1 ,.1 ))
		sizeMenu = (119/800.0*screenSize[0],43/600.0*screenSize[1])
		s.textureIdButtonMenu = TextureLoader.load( os.path.join('assets', 'screenGame','bttnBack.png'),sizeMenu)

		s.bttnMenu =	KButton(0, 554/600.0*screenSize[1], sizeMenu[0],sizeMenu[1],  s.textureIdButtonMenu,True)
		s.arrButtons =	[s.bttnMenu]

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
	def initEvents(s):
		s.EVENT_MENU=[]

	def initBackground(s,screen,resolution):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0 )

		s.helperRenderScreen(screen ,s.arrButtons)
		s.helperRenderScreen(screen ,s.arrIcnText)
		pass

	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		self.CLICK_BUTTONS()

	def CLICK_BUTTON_MENU(self): self.helperRaiseEvent(self.EVENT_MENU)

	def CLICK_BUTTONS(self):
		mousePos = pygame.mouse.get_pos()
		bttn_event = [
			[self.bttnMenu, self.CLICK_BUTTON_MENU]]
		for bttn,event in bttn_event:
			if( not bttn.isUnder(mousePos)):continue
			event()
			return  True
		return False

	def renderUpdate(self, timeElapsed):
		self.icnMouse.pos = pygame.mouse.get_pos()
		
		