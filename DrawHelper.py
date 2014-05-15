import pygame
import TextureLoader

screenSize = [0,0]; #width and height
def init(width,height):
	global screenSize
	screenSize = [width,height];
	pass

def drawAspect(screen,textureId, x,y): #drawing in terms of aspect 
	global screenSize
	screen.blit(TextureLoader.get( textureId), (x*screenSize[0],y*screenSize[1]) ); 
	#screen.blit(TextureLoader.get( textureId), pygame.Rect(50,50,10,10) ); 
	#pygame.draw.rect(screen,(255,0,0),(200,150,100,50))
	pass
def drawCoor(screen,textureId, x,y,w,h): #drawing i nterms of raw coordinates
	pass