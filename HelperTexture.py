import pygame
import TextureLoader

def scale(img,ratio):
	return pygame.transform.scale(img, (int(ratio[0]) , int(ratio[1]) ) )
def scaleId(id,ratio):
	img = TextureLoader.get(id)
	return pygame.transform.scale(img, (int(ratio[0]) , int(ratio[1]) ) )