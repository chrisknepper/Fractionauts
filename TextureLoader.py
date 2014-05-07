import pygame
import HelperTexture
id = 0;
textures = {}
def helperRescale(img,scale):
	return pygame.transform.scale(img, (int(scale[0]) , int(scale[1]) )  )
def load(osPath, scale =()):
	global id;
	id += 1;
	myId = id;
	img = pygame.image.load(osPath).convert_alpha();
	if(scale != () ) : img =HelperTexture.scale(img,scale)

	textures[myId] =   img
	return myId;

def get(id):
	return textures[id];