import pygame

class EasyLine():
	def __init__(s, pFrom, pTo, color , width ):
		s.color = color
		s.width = width
		s.pointFrom = pFrom
		s.pointTo = pTo
		s.rect = (0,0,0,0)
	def draw(s, screen):
		s.rect = pygame.draw.line(screen, s.color, s.pointFrom, s.pointTo, s.width)
		return s.rect


