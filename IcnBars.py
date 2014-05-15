import pygame
import HelperVec2
import os
from IcnBasic import IcnBasic
import TextureLoader
import HelperTexture

class IcnBars (IcnBasic):
	RATIO_DIV_HEIGHT  = .1
	#textureIdDiv=-1,textureIdFill = -1, textureIdWave = -1
	def __init__(self, x, y, w, h, count=10 , isTextureNeedResize = False):
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

		self.textureDiv =	TextureLoader.get( TextureLoader.load(os.path.join('assets', 'IcnBars','fuelDiv.png' ),	(w,h*.04) ) );
		self.textureFill =	TextureLoader.get( TextureLoader.load(os.path.join('assets', 'IcnBars','fuelFill.png' ), 	(w,h) )  );
		self.textureWave =	TextureLoader.get( TextureLoader.load(os.path.join('assets', 'IcnBars','wave.png' ),	(w, 3) ) );#deprecated


		self.aniFluidMove = 0
		self.aniFluidWidth = self.textureWave.get_width()

		#surface to overdrawn on top ok?

		#if(isTextureNeedResize): self.textureDiv = HelperTexture.scale(self.textureDiv,( w , self.textureDiv.get_height() ) )
		pass

	def renderDivs(self, surface, texture,  nums):
		barHeight = self.size[1] / nums
		for i in range (1,nums):
			surface.blit(texture,  (self.pos[0],self.pos[1]+ barHeight * i ) )	

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
		self.aniTimeMax = .8

		#self.helperFillBars(self.mySurface, self.cellHeight, self.textureDiv, 0, n)


	def drawWave(self, pos,surface = -1):
		self.aniFluidMove = (self.aniFluidMove+.1) % self.aniFluidWidth

		surface.blit(self.textureWave, (pos[0] -self.aniFluidMove,pos[1]) )
		surface.blit(self.textureWave, (pos[0]-self.aniFluidMove + self.aniFluidWidth, pos[1] ) )
		pass

	def updateMySurface(self,surface):
		pygame.draw.rect(surface, (0,0,0), (self.pos[0],self.pos[1], self.size[0],self.size[1] +1) )
		height = int(self.size[1] * self.fillRatio) 
		top =  (self.pos[0],self.pos[1]+ self.size[1] -height) 
		surface.blit(self.textureFill ,top, (0,0, self.size[0],height) )
		self.renderDivs( surface, self.textureDiv, self.count)

	def drawUpdate(self, timeElapsed,surface = -1 ):
		if(not self.isAnimation): 
			if(self.stateRender is self.STATE_RENDER_ENABLED):
				self.renderDisable()
			return False
		if(surface is -1 ): surface = self.mySurface

		self.aniTimeElapsed += timeElapsed
		progress = self.aniTimeElapsed / float(self.aniTimeMax)
		progress = min(progress,1.0)
		self.isAnimation = progress != 1.0
		
		ratio = (1 - (progress-1 )*(progress-1 ))
		ratio += (1-ratio)*progress
		self.fillRatio = self.fillRatioBegin + self.fillRate * ratio
		
		self.updateMySurface(surface)
		return True