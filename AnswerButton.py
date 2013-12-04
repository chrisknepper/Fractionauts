import pygame
from Container import Container

class AnswerButton(Container):

    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0,255,0)
        #self.image = pygame.image.load(filename)
        self.text = text
