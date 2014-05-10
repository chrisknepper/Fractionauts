import pygame
import HelperTexture
id = 0;
textures = {}
dicTextureIds = {}
def helperRescale(img,scale):
	return pygame.transform.scale(img, (int(scale[0]) , int(scale[1]) )  )
def load(osPath, scale =()):
	idGenerated = str(osPath) + str(scale)
	if( idGenerated in dicTextureIds) : 
		print "TextureLoader DUPLICATED LOAD CALLS"
		return dicTextureIds[idGenerated]

	global id;
	id += 1;
	img = pygame.image.load(osPath).convert_alpha();
	if(scale != () ) : img =HelperTexture.scale(img,scale)

	dicTextureIds[idGenerated] = id
	textures[id] =   img
	return id;

def get(id):
	return textures[id];