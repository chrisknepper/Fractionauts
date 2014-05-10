import pygame
import HelperVec2
from IcnBasic import IcnBasic
import TextureLoader
import HelperTexture

class IcnBars (IcnBasic):
	RATIO_DIV_HEIGHT  = .1
	def __init__(self, x, y, w, h, count=10 ,textureIdDiv=-1,textureIdFill = -1, textureIdWave = -1, isTextureNeedResize = False):
		IcnBasic.__init__(self,x,y,w,h)
		
		self.fillRatio  = 0
		self.fillRatioBegin = 0
		self.fillRate = 0;

		self.isAnimation = False
		self.aniTimeElapsed = 0
		self.aniTimeMax = 0



		self.count = count;
		self.mySurface = pygame.Surface((w,h))
		self.surfaceTop = pygame.Surface( (w,h),pygame.SRCALPHA  )
		self.cellHeight = h/ count
		self.textureDiv = pygame.Surface((0,0)) if textureIdDiv is -1 else TextureLoader.get(textureIdDiv);
		self.textureFill = pygame.Surface((0,0)) if textureIdFill is -1 else TextureLoader.get(textureIdFill);
		self.textureWave = pygame.Surface((0,0)) if textureIdWave is -1 else TextureLoader.get(textureIdWave);


		self.aniFluidMove = 0
		self.aniFluidWidth = self.textureWave.get_width()

		print "height  is "+str( self.textureDiv.get_height() )
		print "but my height  is " + str(self.cellHeight)
		#surface to overdrawn on top ok?

		#if(isTextureNeedResize): self.textureDiv = HelperTexture.scale(self.textureDiv,( w , self.textureDiv.get_height() ) )
		pass

	def renderDivs(self, surface, texture,  nums):
		surface.fill((0,0,0,0) )
		barHeight = self.size[1] / nums
		for i in range (1,nums):
			surface.blit(texture,  (0, barHeight * i ) )	

		pass

	#currently takiing number of sticks to draw
	#render percentage! not blocks needs dratstic changes to be made 
	def helperFillBars(self,surface, height, texture , indexFrom,indexTo):
		surface.fill((0,0,0) )
		for i in range(indexFrom,indexTo):
			surface.blit(texture, (0,   height * self.count -height* (i+1) ) )
			#pygame.draw.rect(surface,(200,100,0), (0, height* i, 1000, height ))
		pass

	#potential loss of detail of texture due to rescale
	#work on it if issue rises
	def setCount(self, n ):
		self.count = n
		self.renderDivs(self.surfaceTop,self.textureDiv,  self.count)
		self.mySurface.blit(self.surfaceTop,(0,0))
		#self.textureDiv = HelperTexture.scale(self.textureDiv,(self.size[0],self.cellHeight) )

	def display(self, n ):
		self.fillRatioBegin = self.fillRatio
		fillRatioTo = max(min( n, 1),0)
		self.fillRate = fillRatioTo - self.fillRatioBegin

		self.isAnimation = True
		self.aniTimeElapsed = 0
		self.aniTimeMax = 1.0

		#self.helperFillBars(self.mySurface, self.cellHeight, self.textureDiv, 0, n)


	def drawWave(self, pos):
		self.aniFluidMove = (self.aniFluidMove+1) % self.aniFluidWidth

		self.mySurface.blit(self.textureWave, (pos[0] -self.aniFluidMove,pos[1]) )
		self.mySurface.blit(self.textureWave, (pos[0]+ self.aniFluidWidth-self.aniFluidMove , pos[1] ) )
		pass

	def drawUpdate(self, timeElapsed ):
		if(self.isAnimation):
			self.aniTimeElapsed += timeElapsed
			progress = self.aniTimeElapsed / float(self.aniTimeMax)
			progress = min(progress,1.0)
			self.fillRatio = self.fillRatioBegin + self.fillRate * progress
			self.isAnimation = progress != 1.0
		
		self.mySurface.fill((0, 0, 0)) 
		top =  (0, self.size[1] - self.size[1] * self.fillRatio ) 
		self.mySurface.blit(self.textureFill ,top)
		self.drawWave(top)
		self.mySurface.blit(self.surfaceTop,(0,0))
		pass