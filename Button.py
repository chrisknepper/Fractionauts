import pygame


class Button:

    def __init__(self, x, y, width, height, text, color=(0, 0, 255)):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textObj = self.fontObj.render(text, True, (0, 255, 0))
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (x + (width / 2), y + (height / 2))
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (
            self.x, self.y, self.width, self.height), 0)
        screen.blit(self.textObj, self.textRectObj)

    def is_under(self, pos):
        x, y = pos
        if (self.x < x and
            self.x + self.width > x and
            self.y < y and
            self.y + self.height > y
            ):
            #print 'You are under a button!'
            return pos
        else:
            return None
