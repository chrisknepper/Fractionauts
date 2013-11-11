import pygame


class Background(object):

    def __init__(self, filename):
        self.image = pygame.image.load(filename)

    def draw(self):
        pygame.transform.scale(
            self.image,
            (pygame.display.Info().current_w, pygame.display.Info().current_h)
        )
        screen.blit(self.image, (self.x, self.y))
