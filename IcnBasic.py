import pygame
import TextureLoader
import HelperTexture

class IcnBasic:
	STATE_RENDER_ENABLED=0
	STATE_RENDER_PAUSE_NORMAL = 1
	STATE_RENDER_PAUSE_STATIC = 2 #static pause means drawing onto background 
	STATE_RENDER_PAUSE_END = 3 
	def EVENT_STATIC_NOW(me):
		for e in me.EVENHDR_STATIC : e(me)
	def registerEvent_static(me, e):
		me.EVENHDR_STATIC.append(e)

	def setRenderStatic(s, surface):
		s.isRenderStatic = True
		s.surfaceBG = surface
	
	@staticmethod
	def FROM_PATH( path):
		id = TextureLoader.load(path)
		texture = TextureLoader.get(id)
		return IcnBasic(0,0, texture.get_width(),texture.get_height(),id)


	def __init__(me,x,y,w,h,textureID=-1,isTextureRescaled = False):
		me.isSelected = False
		me.isRenderStatic = False
		me.stateRender = me.STATE_RENDER_ENABLED

		me.EVENHDR_STATIC = []

		me.pos = (x,y)
		me.size = (w,h)
		me.textureID = textureID
		me.rect = (0,0,10,10);
		me.mySurface = pygame.Surface((w,h),pygame.SRCALPHA) if textureID is -1 else TextureLoader.get(textureID)
		if(isTextureRescaled ) : me.mySurface =HelperTexture.scale(me.mySurface, me.size)
		
	def setSelect(s,value):
		s.isSelected = value
		
	def isUnder(me,pos):
		x, y = pos
		if (me.pos[0] < x and
			me.pos[0] + me.size[0] > x and
			me.pos[1] < y and
			me.pos[1] + me.size[1] > y
			):
			return pos
		else: return None
		
	def select(me):
		me.isSelected = not me.isSelected
		return me.isSelected
	def renderEnable(me):
		me.stateRender = me.STATE_RENDER_ENABLED
	def renderDisable(me):
		me.stateRender = me.STATE_RENDER_PAUSE_STATIC if me.isRenderStatic\
					else me.STATE_RENDER_PAUSE_NORMAL  

	def helperDraw(me, screen):
		return screen.blit(me.mySurface,me.pos)

	def draw(me,screen):
		if(me.stateRender is me.STATE_RENDER_ENABLED ):
			me.rect = me.helperDraw(screen)
		elif(me.stateRender is me.STATE_RENDER_PAUSE_NORMAL):
			me.stateRender = me.STATE_RENDER_PAUSE_END
			me.helperDraw(screen)
			me.rect  = (0,0,0,0)
		
		elif(me.stateRender is me.STATE_RENDER_PAUSE_STATIC):
			me.stateRender = me.STATE_RENDER_PAUSE_END
			me.helperDraw(me.surfaceBG)
			me.rect = me.helperDraw(screen)
			me.stateRender = me.STATE_RENDER_PAUSE_NORMAL

		elif(me.stateRender is me.STATE_RENDER_PAUSE_END):
			return me.rect
		return me.rect
	
	def drawUpdate(me, timeElapsed=0):
		return False