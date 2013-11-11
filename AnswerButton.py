import pygame
import Button

class AnswerButton(Button):

    def __init__(self, x, y, width, height, filename, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(filename)
        self.text = text

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
