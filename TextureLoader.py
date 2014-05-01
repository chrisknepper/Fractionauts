import pygame

id = 0;
textures = {}
def load(osPath, scale =()):
	global id;
	id += 1;
	myId = id;
	img = pygame.image.load(osPath).convert_alpha();
	if(scale != () ) : img = pygame.transform.scale(img, scale)

	textures[myId] =   img
	return myId;

def get(id):
	return textures[id];