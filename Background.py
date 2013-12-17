import pygame


class Background(object):

    def __init__(self, filename, x = 0, y = 0):
        self.image = pygame.image.load(filename)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.transform.scale(
            self.image,
            (pygame.display.Info().current_w, pygame.display.Info().current_h)
        )
        screen.blit(self.image, (self.x, self.y))
