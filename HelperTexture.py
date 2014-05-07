import pygame

def scale(img,ratio):
	return pygame.transform.scale(img, (int(ratio[0]) , int(ratio[1]) ) )